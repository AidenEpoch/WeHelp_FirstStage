from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import urllib.parse
import urllib.request
import json

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="wehelp_secret_key")

HOTELS_CH_URL = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
HOTELS_EN_URL = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

def fetch_hotel_by_id(hotel_id):
    url_ch = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
    url_en = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

    try:
        req_ch = urllib.request.Request(
            url_ch,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req_ch) as response:
            data_ch = json.loads(response.read().decode("utf-8"))["list"]

        req_en = urllib.request.Request(
            url_en,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req_en) as response:
            data_en = json.loads(response.read().decode("utf-8"))["list"]

        print(hotel_id)
        target_id = int(hotel_id)


        hotel_ch = None
        for hotel in data_ch:
            if hotel["_id"] == target_id:
                hotel_ch = hotel
                break

        hotel_en = None
        for hotel in data_en:
            if hotel["_id"] == target_id:
                hotel_en = hotel
                break

        if hotel_ch is None:
            return None

        return {
            "name": hotel_ch["旅宿名稱"],
            "eng_name": hotel_en["hotel name"] if hotel_en else "",
            "tel": hotel_ch["電話或手機號碼"]
        }

    except Exception as e:
        print("fetch_hotel_by_id Error:", e)
        return None
    
@app.get("/")
async def home():
    return FileResponse("templates/index.html")


@app.post("/login")
async def login(request: Request, email: str = Form(None), password: str = Form(None)):
    if not email or not password:
        error_msg = urllib.parse.quote("請輸入信箱和密碼")
        return RedirectResponse(url=f"/ohoh?msg={error_msg}", status_code=303)
    
    if email == "abc@abc.com" and password == "abc":
        request.session["LOGGED-IN"] = True
        return RedirectResponse(url="/member", status_code=303)
    else:
        error_msg = urllib.parse.quote("帳號、或密碼輸入錯誤")
        return RedirectResponse(url=f"/ohoh?msg={error_msg}", status_code=303)


@app.get("/member")
async def member(request: Request):
    if not request.session.get("LOGGED-IN"):
        return RedirectResponse(url="/", status_code=303)
        
    return FileResponse("templates/member.html")


@app.get("/logout")
async def logout(request: Request):
    request.session["LOGGED-IN"] = False
    return RedirectResponse(url="/", status_code=303)


@app.get("/ohoh")
async def error_page():
    return FileResponse("templates/error.html")


@app.get("/hotel/{hotel_id}")
async def hotel_page(hotel_id: str):
    return FileResponse("templates/hotel.html")


@app.get("/api/hotel/{hotel_id}")
def api_hotel(hotel_id: str):
    hotel_info = fetch_hotel_by_id(hotel_id)

    if hotel_info is None:
        return {
            "success": False,
            "message": "查詢不到相關資料"
        }

    return {
        "success": True,
        "data": hotel_info
    }