##def w1(func):
##            def inner():
##                        print('验证')
##                        func()
##            return inner
##
##def f1():
##            print('---f1---')
##
##def f2():
##            print('---f2---')
##
##f1 = w1(f1)
##f1()



##def w1(func):
##            def inner():
##                        print('验证')
##                        func()
##            return inner
##
###自动执行w1和inner,并把f1传到了w1,且f1指向了inner
##@w1
##def f1():
##            print('---f1---')
##
##@w1
##def f2():
##            print('---f2---')
##
##f1()


##有参数的装饰器
##def w1(func):
##            #*args和**kwargs用其中之一即可，（元组和字典）
##            def inner(*args,**kwargs):
##                        print('验证')
##                        func(*args)
##            return inner
##
###自动执行w1和inner,并把f1传到了w1,且f1指向了inner
##@w1
##def f1(a,b,c):
##            print('---f1---a=%d and b=%d and c=%d'%(a,b,c))
##
##@w1
##def f2():
##            print('---f2---')
##
##f1(11,12,100)



##通用装饰器
def w1(func):
            #*args和**kwargs用其中之一即可，（元组和字典）
            def inner(*args,**kwargs):
                        print('验证')
                        ret = func(*args,**kwargs)
                        return ret
            return inner

#自动执行w1和inner,并把f1传到了w1,且f1指向了inner
@w1
def f1(a,b,c):
            print('---f1---a=%d and b=%d and c=%d'%(a,b,c))

@w1
def f2():
            print('---f2---')
            return 'xman'

print(f1(11,12,100))
print(f2())


##带有 参数的装饰器
def func_arg(arg):
            def w1(func):
                        #*args和**kwargs用其中之一即可，（元组和字典）
                        def inner(*args,**kwargs):
                                    print('验证')
                                    ret = func(*args,**kwargs)
                                    return ret
                        return inner
            return w1

#自动执行w1和inner,并把f1传到了w1,且f1指向了inner
#1、先执行func_arg()
#2、再@w1对f1进行装饰，使f1指向inner
@func_arg('haha')
def f1(a,b,c):
            print('---f1---a=%d and b=%d and c=%d'%(a,b,c))

@func_arg('xixi')
def f2():
            print('---f2---')
            return 'xman'

print(f1(11,12,100))
print(f2())

