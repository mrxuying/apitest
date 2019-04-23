##import sys
##
##class Test:
##            def __del__(self):
##                   print("---over---")
##
##t1 = Test()
##t2 = t1
##
##del t1
##count = sys.getrefcount(t2)       ##数引用的对象的个数，因为自身调用会多一个，所以比实际存在的对象多1
##print(count)
##del t2
##sys.getrefcount(t2)
##count = sys.getrefcount(t2) #测量引用对象的个数
##print(count)
##print('======================')

##class Animal(object):
##            def eat(self):
##                        print('吃')
##
##            def drink(self):
##                        print('喝')
##
##            def sleep(self):
##                        print('睡')
##class Dog(Animal):
##            def bark(self):
##                        print('汪汪汪')
##            def eat(self):
##                        print('囫囵吞枣')
##                        ##Dog.eat(self)           #调用被重写的父类方法的第一种，self必须要写上
##                        super().eat()           #调用被重写的父类方法的第二种
##
##class Doge(Animal,Dog):
##            pass
##
##dog1 = Dog()
##
##dog1.eat()
##super().eat()           #调用被重写的父类方法的第二种


##多态
##class Dog(object):
##            def print_self(self):
##                        print('A')
##
##class Doge:
##            def print_self(self):
##                        print('B')
##
##def introduce(temp):
##            temp.print_self()
##dog1 = Dog()
##dog2 = Doge()
##
##introduce(dog1)
##introduce(dog2)


class Tool(object):

            num = 0
            def __init__(self,new_name):
                        self.name = new_name
                        Tool.num += 1

tool1 = Tool('螺丝刀')
tool2 = Tool('指甲剪')
tool3 = Tool('汤勺')

print(Tool.num)




class Game(object):

            num = 0
##实例方法
            def __init__(self):
                        self.name = 'laoxu'
##类方法
            @classmethod
            def add_num(cls):
                        cls.num = 100

#静态方法
            @staticmethod
            def print_menu():
                        print('----star----')
                        print('----moon----')
                        print('----sea----')

g1 = Game()
Game.print_menu()




                        































