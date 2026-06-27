import urllib.request as request
import bs4
import csv

url = "https://www.ptt.cc/bbs/Steam/index.html"



#with open("page.txt", "w", encoding="utf-8") as file:
 #   file.write(data)

strLine = []
for i in range(3):
    requestObj = request.Request(url, headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
})

    with request.urlopen(requestObj) as response:
        data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(data, "html.parser")
        titles = root.find_all("div", class_ = "r-ent")  #titles 會是一個 list item 為「div 標籤以及其內容文字」的一個 list

    for realTitle in titles:
        name = realTitle.find("a")
        likeCount = realTitle.find("div", class_ = "nrec")
        if likeCount.string == None:
            likeCount.string = " "
        if name == None:
            name = realTitle.find("div", class_="title")
           # print(f"{name.string.strip()},{likeCount.string.strip()},")
            continue
        link = name.get("href")
        urlNew = "https://www.ptt.cc"
        insideLink = urlNew + link
        #print(f"insideLink = {insideLink}")
        requestInside = request.Request(insideLink, headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
        })
        with request.urlopen(requestInside) as response:
            dataInside = response.read().decode("utf-8")
        rootInside = bs4.BeautifulSoup(dataInside, "html.parser")
        time = rootInside.find_all("span", class_="article-meta-value")
        if len(time) != 0:
            realTime = time[3]
            #print(f"{name.string},{likeCount.string},{realTime.string}")
            strTemp = f"{name.string},{likeCount.string},{realTime.string}"
            strLine.append(strTemp)
        else:
            if name.string == "[公告] 板務宣導/實用連結/置底聊天區":
                realTime = rootInside.find("span", class_="f2 b2")
                timeIndex = realTime.string.find(", ")
                realTimeString = realTime.string[timeIndex+2:]
                #print(f"{name.string},{likeCount.string},{realTimeString}")
                strTemp = f"{name.string},{likeCount.string},{realTimeString}"
                strLine.append(strTemp)
            elif name.string == "[公告] 交易文章使用說明(發文/推文前請詳閱)":
                realTime = rootInside.find_all("span", class_="b4")[3]
                #timeIndex = realTime.string.find(", ")
                #realTimeString = realTime.string[timeIndex+2:]
                #print(f"{name.string},{likeCount.string},{realTimeString}")
                #print(f"{name.string},{likeCount.string},{realTime.string}")
                strTemp = f"{name.string},{likeCount.string},{realTime.string}"
                strLine.append(strTemp)
            elif "置底遊戲交換區" in name.string:
                realTime = rootInside.find_all("span", class_="f2")[2]
                timeIndex = realTime.string.find(", ")
                realTimeString = realTime.string[timeIndex+2:]
                #print(f"{name.string},{likeCount.string},{realTimeString}")
                strTemp = f"{name.string},{likeCount.string},{realTimeString}"
                strLine.append(strTemp)
            else:
                realTime = rootInside.find_all("span", class_="b4")[3]
                #print(f"{name.string},{likeCount.string},{realTime.string}")
                strTemp = f"{name.string},{likeCount.string},{realTime.string}"
                strLine.append(strTemp)
    newPage = root.find_all("a", class_="btn wide")[1].get("href")
    url = "https://www.ptt.cc" + newPage

with open("articles.csv", "w", encoding="utf-8") as csvFile:
    writer = csv.writer(csvFile)
    for article in strLine:
        #article = article + "\n"
        article = article.split(",")
        writer.writerow(article)
