import urllib.request as request
import json
src1 = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
src2 = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"
with request.urlopen(src1) as response:
    data1 = json.load(response)

with request.urlopen(src2) as response:
    data2 = json.load(response)

innList1 = data1["list"]
innList2 = data2["list"]
innOrderChinese = []
innOrderEnglish = []
innChineseName = []
innEnglishName = []
innChineseAddr = []
innEnglishAddr = []
innPhone = []
innRoomCount = []
for i in range(len(innList1)):
    innOrderChinese.append(innList1[i])

for i in range(len(innList2)):
    innOrderEnglish.append(innList2[i])

innOrderChinese.sort(key = lambda Inn: Inn["_id"])
innOrderEnglish.sort(key = lambda Inn: Inn["_id"])

with open("hotels.csv", "w", encoding="utf-8") as file:
    for i in range(len(innOrderChinese)):
        str = innOrderChinese[i]["旅宿名稱"] + "," + innOrderEnglish[i]["hotel name"] + "," + innOrderChinese[i]["地址"] + "," + innOrderEnglish[i]["address"] + "," + innOrderChinese[i]["電話或手機號碼"] + "," + innOrderChinese[i]["房間數"] + "\n"
        file.write(str)

district_hotels = {}
district_rooms = {}
for i in range(len(innOrderChinese)):
    if innOrderChinese[i]["地址"][3:6] not in district_hotels:
        district_hotels[innOrderChinese[i]["地址"][3:6]] = 1
        district_rooms[innOrderChinese[i]["地址"][3:6]] = int(innOrderChinese[i]["房間數"])
    elif innOrderChinese[i]["地址"][3:6] in district_hotels:
        district_hotels[innOrderChinese[i]["地址"][3:6]] += 1
        district_rooms[innOrderChinese[i]["地址"][3:6]] += int(innOrderChinese[i]["房間數"])

with open("districts.csv", "w", encoding="utf-8") as file:
    for innName in district_hotels.keys():
        str = f"{innName},{district_hotels[innName]},{district_rooms[innName]}\n"
        file.write(str)

