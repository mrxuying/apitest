##集合可以对列表进行去重

list1 = [1,21,3,2,3,5,3,6,5,8,6,9,5,4]
b = set(list1)
list1 = list(b)
print(list1)

##可以进行求交集，并集
