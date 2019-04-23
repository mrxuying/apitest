ret = map(lambda x:x*x, [1,2,3])
for i in ret:
            print(i)
result = map(lambda x,y:x+y, [1,2,3],[4,5,6])
for j in result:
            print(j)

def func(x, y):
            return (x,y)

list1 = [0,1,2,3,4,5,6]
list2 = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
list3 = map(func ,list1 , list2)
print(list(list3))


##filter函数
rest = filter(lambda x:x%2 , [1,2,3,4])         ##自动过滤掉为不为真的数据，保存为真的数据，并去重
print(list(rest))


test = filter(None , ['she',0])
print(list(test))


##reduce函数
from functools import reduce
test0 = reduce(lambda x,y:x+y, ['aa','bb','cc'],'dd')
print(test0)
