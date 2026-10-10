from datetime import datetime
if len((open("money.txt","r").readline())) != 0:
    a = int(open("money.txt","r").readline())
else:
    print("輸入現有的金額")
    a = int(input())
t = datetime.now()
x = ""
while x != "Q":
    print("輸入T存入F取出E查看現有金額Q離開")
    x = input()
    if x == "T":
        while True:
            try:
                b = int(input("輸入存入的金額：\n"))
                break
            except ValueError:
                print("請輸入有效的整數！\n")
        a += b
        print("存入後的金額為" + str(a))
        t = datetime.now()
        with open("moneytime.txt","a",encoding="utf-8")as f:
            f.write(str(t)+"\t存入"+str(b)+"\n")
    elif x == "F":
        while True:
            try:
                c = int(input("輸入取出的金額：\n"))
                break
            except ValueError:
                print("請輸入有效的整數！\n")
        a -= c
        print("取出後的金額為" + str(a))
        t = datetime.now()
        with open("moneytime.txt","a",encoding="utf-8")as f:
            f.write(str(t)+"\t取出"+str(c)+"\n")
    elif x == "E":
        print("現有的金額為" + str(a))
    elif x == "Q":
        print("離開程式")
        break
    else:
        print("輸入錯誤請重新輸入")

open("money.txt","w").write(str(a))





