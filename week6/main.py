from fastapi import FastAPI, Request, Body
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse
import mysql.connector
import json

con=mysql.connector.connect(
    user="root",
    password="12345",
    host="localhost",
    database="websiteWeek6"
)
print("Database Ready")

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key = "WeHelp")

templates=Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )


@app.get("/member")
async def member(request: Request):
    if request.session["member"] == None:
        return templates.TemplateResponse(
        request=request, name="index.html"
    )
    return templates.TemplateResponse(
        request=request, name="member.html", context={"name": request.session["member"]["name"]}
    )


@app.get("/ohoh")
async def ohoh(request: Request, msg):
    return templates.TemplateResponse(
        request=request, name="ohoh.html", context={"msg": msg}
    )



@app.post("/signup")
async def signUp(body=Body(None)):
    body=json.loads(body)
    name=body["name"]
    email=body["email"]
    password=body["password"]
    cursor = con.cursor()
    cursor.execute("SELECT * FROM member WHERE email = %s", [email])
    result=cursor.fetchone()
    if result == None:
        cursor.execute("INSERT INTO member(name, email, password)VALUES(%s, %s, %s)", [name, email, password])
        con.commit()
        return {"ok": True}
    else:
        return {"ok": False}


@app.post("/login")
async def logIn(request: Request, body=Body(None)):
    body=json.loads(body)
    email=body["email"]
    password=body["password"]
    cursor = con.cursor()
    cursor.execute("SELECT * FROM member WHERE email = %s AND password = %s", [email, password])
    result=cursor.fetchone()
    if result == None:
        request.session["member"] = None
        return {"ok": False}
    else:
        request.session["member"] = {
            "name": result[1],
            "email": result[2]
        }
        return {"ok": True}
    

@app.get("/logout")
async def logOut(request: Request):
    request.session["member"] = None
    return RedirectResponse("/")


@app.post("/api/message")
async def createMessage(request:Request, body=Body(None)):
    #body = json.loads(body)
    current_email = request.session["member"]["email"]
    content=body["content"]
    if content == None or content.strip() == "":
        return {"error": True}
    cursor = con.cursor()
    cursor.execute("SELECT id FROM member WHERE email = %s", [current_email])
    author_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO message(author_id, content) VALUES(%s, %s)", [author_id, content])
    con.commit()
    return {"ok": True}


@app.get("/api/message")
async def getMessage(request:Request):
    if request.session["member"] == None:
        return {"error": True}
    current_email = request.session["member"]["email"]
    cursor = con.cursor(dictionary = True)
    query = """SELECT message.id, member.name, message.content, member.email FROM message 
                JOIN member ON message.author_id = member.id ORDER BY message.create_time ASC"""
    cursor.execute(query)
    rows = cursor.fetchall()

    message_list = []
    for row in rows:
        message_list.append({
            "id": row["id"],
            "name": row["name"],
            "content": row["content"],
            "self": row["email"] == current_email
        })
    
    return {"ok": True, "data": message_list}


@app.delete("/api/message/{message_id}")
async def delete_message(request: Request, message_id: int):
    if request.session["member"] == None:
        return {"error": True}
        
    current_email = request.session["member"]["email"]
    
    cursor = con.cursor()
    query = """
        SELECT message.id FROM message 
        JOIN member ON message.author_id = member.id 
        WHERE message.id = %s AND member.email = %s
    """
    cursor.execute(query, [message_id, current_email])
    result = cursor.fetchone()
    
    if result == None:
        return {"error": True}
    
    cursor.execute("DELETE FROM message WHERE id = %s", [message_id])
    con.commit()
    return {"ok": True}

    
app.mount("/static", StaticFiles(directory="static"), name="static")


