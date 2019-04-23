import functools

def showarg(*args, **kwargs):
            print(args)
            print(kwargs)

f1 = functools.partial(showarg,1,2,3)           ##偏函数partial,固定的参数可以不用在调用的时候再传

f1()
f1(4,5,6)
f1(a='python',b='itcast')

f2 = functools.partial(showarg,a=3,b='linux')
f2()
f2(7,8,9)
f2(a='python',b='itcast')
