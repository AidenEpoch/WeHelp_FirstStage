print("=== Task1 ===")
def func1(name):
    char = {"悟空": (0, 0), "辛巴": (-3, 3), "丁滿": (-1, 4), "貝吉塔": (-4, -1),  "特南克斯": (1, -2), "弗利沙": (4, -1)}
    #線的方程式大概是: 5x + 4y = 7
    s1 = set()      #左下方
    s2 = set()     #右上方
    for key, value in char.items():
        if 5 * value[0] + 4 * value[1] <= 7:
            s1.add(key)
        else:
            s2.add(key)
    distance = {}
    for key, value in char.items():
        if key == name:
            continue
        else:
            if name in s1 and key in s1:
                distance[key] = abs(char[name][0] - value[0]) + abs(char[name][1] - value[1])
            elif name in s1 and key in s2:
                distance[key] = abs(char[name][0] - value[0]) + abs(char[name][1] - value[1]) + 2
            elif name in s2 and key in s1:
                distance[key] = abs(char[name][0] - value[0]) + abs(char[name][1] - value[1]) + 2
            else:
                distance[key] = abs(char[name][0] - value[0]) + abs(char[name][1] - value[1])
    far = []
    near = []
    max_dist = max(distance.values())
    min_dist = min(distance.values())
    for key, value in distance.items():
        if value == max_dist:
            far.append(key)
        elif value == min_dist:
            near.append(key)
    print(f"最遠", end="")
    for i in range(len(far)):
        if i != 0:
            print(f"、{far[i]}", end="")
        else:
            print(f"{far[i]}", end="")
    print(f"；最近", end="")
    for i in range(len(near)):
        if i != 0:
            print(f"、{near[i]}", end="")
        else:
            print(f"{near[i]}", end="")
    print()
    


func1("辛巴") # print 最遠弗利沙；最近丁滿、貝吉塔
func1("悟空") # print 最遠丁滿、弗利沙；最近特南克斯
func1("弗利沙") # print 最遠辛巴，最近特南克斯
func1("特南克斯") # print 最遠丁滿，最近悟空

print(f"=== Task2 ===")
ss_schedules = {}
def func2(ss, start, end, criteria):
    for s in ss:
        if s["name"] not in ss_schedules:
            ss_schedules[s["name"]] = [False] * 25
    #以下是有彈性且普遍的寫法，將criteria分成3個種類，分別是name, c(cost)和r(rating)
    #3種不同類別分別會對應不同的「值區間」(名字、數字等等)
    if ">=" in criteria:       #必跟r或c有關
        op = ">="
        category, value = criteria.split(">=")
    elif "<=" in criteria:     #必跟r或c有關
        op = "<="
        category, value = criteria.split("<=")
    elif "=" in criteria:      #必跟name有關
        op = "="
        category, value = criteria.split("=")
    if op != "=":
        value = float(value)       #因為數字不一定是整數，所以要轉成floating number，轉成數字對應的函式有int(), float()
    candidates = []                #先將符合的抓出來
    for s in ss:
        matched = False
        if op == "=" and s[category] == value:
            matched = True
        elif op == ">=" and s[category] >= value:
            matched = True
        elif op == "<=" and s[category] <= value:
            matched = True
        if matched == True:
            available = True
            for i in range(start, end):
                if ss_schedules[s["name"]][i] == True:
                    available = False
                    break
            if available == True:
                candidates.append(s)
    if len(candidates) == 0:        #沒有合適的服務可以選擇
        print("Sorry")
        return
    best_candidate = candidates[0]
    for m in candidates:
        if op == "<=":
            if m[category] >= best_candidate[category]:
                best_candidate = m
        elif op == ">=":
            if m[category] <= best_candidate[category]:
                best_candidate = m
    print(best_candidate["name"])
    for i in range(start, end):
        ss_schedules[best_candidate["name"]][i] = True
    return
    
            
        
    
services=[
{"name":"S1", "r":4.5, "c":1000},
{"name":"S2", "r":3, "c":1200},
{"name":"S3", "r":3.8, "c":800}
]
func2(services, 15, 17, "c>=800") # S3
func2(services, 11, 13, "r<=4") # S3
func2(services, 10, 12, "name=S3") # Sorry
func2(services, 15, 18, "r>=4.5") # S1
func2(services, 16, 18, "r>=4") # Sorry
func2(services, 13, 17, "name=S1") # Sorry
func2(services, 8, 9, "c<=1500") # S2


print("=== Task3 ===")
def func3(index):
    s = []
    num = 25
    s.append(num)
    for i in range(1, index + 1):
        if i % 4 == 1:
            num -= 2
            s.append(num)
        elif i % 4 == 2:
            num -= 3
            s.append(num)
        elif i % 4 == 3:
            num += 1
            s.append(num)
        else:
            num += 2
            s.append(num)
    print(s[index])
func3(1) # print 23
func3(5) # print 21
func3(10) # print 16
func3(30) # print 6


print("=== Task4 ===")
def func4(sp, stat, n):
    s = []
    for i in range(len(stat)):
        s.append(False)
    index = -1
    for i in range(len(stat)):
        if stat[i] == "0" and sp[i] >= n:
            index = i
            break
    if index != -1:
        for i in range(len(stat)):
            if stat[i] == "0" and sp[i] >= n and sp[i] - n <= sp[index] - n:
                index = i
    else:
        for i in range(len(stat)):
            if stat[i] == "0":
                index = i
        for i in range(len(stat)):
            if stat[i] == "0" and abs(sp[i] - n) <= abs(sp[index] - n):
                index = i
    print(index)
            
func4([3, 1, 5, 4, 3, 2], "101000", 2) # print 5
func4([1, 0, 5, 1, 3], "10100", 4) # print 4
func4([4, 6, 5, 8], "1000", 4) # print 2

