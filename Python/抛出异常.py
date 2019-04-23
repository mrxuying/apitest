class Test(object):
            def __init__(self,switch):
                        self.switch = switch #开关
            def calc(self,a,b):
                        try:
                                    return a/b
                        except Exception as result:
                                    if self.switch:
                                                print('捕获开启，已经捕获到异常，信息如下：')
                                                print(result)
                                    else:
                                                #重新抛出这个异常，此时就不会被这个异常处理给捕获到，从而出发默认异常
                                                raise


a = Test(True)
a.calc(11,0)
f = open('test.txt','wr')
f.write(str(a.calc(11,0)))
b = f.read()
print(b)
f.close

a.switch = False
a.calc(11,0)
