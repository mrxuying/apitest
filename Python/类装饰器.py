class Test(object):
            def __call__(self):
                        print('---test---')

t = Test()
t()
##当对象中有__call__方法时，对象后面加（）调用时就会调用call方法


class Demo(object):
            def __init__(self,func):
                        print('---初始化---')
                        print('func name is %s'%func.__name__)
                        self.__func = func

            def __call__(self):
                        print('---装饰器功能---')
                        self.__func()

@Demo  #与test = Demo(test)意思相同，即使test指向Demo这个类创建的对象，同时将下面的test函数作为参数传给func
def test():
            print('---test---')

test()  #此时调用test方法时相当于调用类Demo中的__call__方法
