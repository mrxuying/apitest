class Itcast(object):
            def __init__(self,subject1):
                        self.subject1 = subject1
                        self.subject2 = 'CPP'

            def __getattribute__(self,obj):                 ##访问属性时一定会先调用这个方法
                        print('====1>%s'%obj)               ##这个方法中不能再使用self来访问其他属性或者方法
                        if obj == 'subject1':
                                    print('log subject1')
                                    return 'redirect python'
                        else:
                                    temp = object.__getattribute__(self, obj)
                                    print('====2>%s'%str(temp))

            def show(self):
                        print('this is Itcast')

s = Itcast('python')
print(s.subject1)
print(s.subject2)
