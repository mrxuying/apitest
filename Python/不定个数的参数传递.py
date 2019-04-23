def fun(a,b,*args,**kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)
c = ("log",18,'love')
d = {"NAME":"MRXU","AGE":18}
fun(11,22,33,44,*c,**d)


def getnum(num):
            if num > 1:
                        num*=getnum(num-1)
                        return num
            else:
                        return num

result = getnum(5)
print(result)
