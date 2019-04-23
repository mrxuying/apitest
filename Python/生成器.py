####列表生成器
##a = [x*2 for x in range(10)]
##print(a)
##
##
##b = (x*2 for x in range(100))
##print(b)
##
##
####斐波拉契数列（Fibonacci）
##def fib():
##            a,b = 0,1
##            while b < 1000:
##                        print(b)
##                        a,b = b,a+b
##
##fib()



def fib():
            a,b = 0,1
            print('---1---')
            while b < 1000:
                        print('---2---')
                        yield b
                        print('---3---')
                        a,b = b,a+b
                        print('---4---')
            print('---5---')

##for i in fib():
##            print(i)
for i in fib():
            print(i)
