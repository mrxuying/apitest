##info = ['name','age','height','sex','high']
##info.sort()
##print(info)
a = 100
def test(num):
            num+=num     ##num指向a=100，100是不可变类型，估该式子只能对num的值进行修改
            print(num)

test(a)
print(a)    


a = [100]
def test(num):
            num+=num     ##num指向a=[100]，[100]是可变类型，估该式子在[100]存储的位置直接修改
            print(num)

test(a)
print(a)    


a = [100]
def test(num):
            num=num+num
            ##num指向a=[100]，[100]是可变类型，但该式子先计算右边的值，会开辟一个新的临时存储位置存储临时的值[num+num]
            print(num)

test(a)
print(a)    


f = open("test.py","w")
f.write("Today is sunny!")
f.close()
g = open("test.py","r")
view = g.read()
print(view)
g.close()



old_file_name = input("要复制的文件名是：")
old_file = open(old_file_name,"r")
content = old_file.read()
position = old_file_name.rfind('.')
new_file_name = old_file_name[0:position]+"[复件]"+old_file_name[position:]
print(new_file_name)
new_file = open(new_file_name,"w")
new_file.write(content)
new_file.close()
old_file.close()
new_file = open(new_file_name,"r")
view = new_file.read()
print(view)
new_file.close()

















