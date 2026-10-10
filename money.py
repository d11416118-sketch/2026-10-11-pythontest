if len((open("money.txt","r").read())) != 0:
    a = int(open("money.txt","r").read())
else:
    print("輸入現有的金額")
    a = int(input())

print("輸入T存入F取出E查看現有金額")
x = input()
if x == "T":
    print("輸入存入的金額")
    b = int(input())
    a += b
    print("存入後的金額為" + str(a))
elif x == "F":
    print("輸入取出的金額")
    c = int(input())
    a -= c
    print("取出後的金額為" + str(a))
elif x == "E":
    print("現有的金額為" + str(a))
else:
    print("輸入錯誤")

open("money.txt","w").write(str(a))







