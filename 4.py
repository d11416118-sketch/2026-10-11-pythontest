#list列表
n = [1,2,3,4,5]
print(n)
print(n[-2])#印出倒數第2個元素
print(n[1:4])#印出第2個到第4個元素
s = ["CC",18,True]
n.extend(s)#將s列表加入n列表
print(n)
n.append("Hello")#在n列表最後加入元素
print(n)
n.insert(1,"World")#在n列表第2個位置加入元素
print(n)
n.remove(3)#移除n列表的元素3
print(n)
n.clear()#清空n列表
print(n)
s.pop()#移除n列表最後一個元素
print(s)
a = [5,2,3,3,5]
a.sort()#排序
print(a)
a.reverse()#反轉
print(a)
print(a.index(5))#找5在哪個位置
print(a.count(3))#計算3出現幾次










