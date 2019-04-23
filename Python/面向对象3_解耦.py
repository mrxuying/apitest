# -*- coding: cp936 -*-
####这样4s店和车类之间就具有耦合性
##class CarStore(object):
##            def order(self,type):
##                        if type == '索纳塔':
##                                    return Suonata()
##                        elif type == '名图':
##                                    return Mingtu()
##
##class Car(object):
##            def move():
##                        print('---run---')
##            def music():
##                        print('---play music---')
##            def stop():
##                        print('---stop---')
##
##class Suonata(Car):
##            def __init__(self):
##                        self.speed_per_second = '180km/s'
##            def __str__(self):
##                        return '最大速度可达：%s'%self.speed_per_second
##
##class Mingtu(Car):
##            def __init__(self):
##                        self.speed_per_second = '210km/s'
##            def __str__(self):
##                        return '最大速度可达：%s'%self.speed_per_second
##           
##order_type = input("购买车型：")
##
##car_store = CarStore()
##car = car_store.order(order_type)
##print(car)              ##for test

##解耦
##class CarStore(object):
##            def order(self,type):
##                        return select_car_type(type)
##
##class Car(object):
##            def move():
##                        print('---run---')
##            def music():
##                        print('---play music---')
##            def stop():
##                        print('---stop---')
##
##class Suonata(Car):
##            def __init__(self):
##                        self.speed_per_second = '180km/s'
##            def __str__(self):
##                        return '最大速度可达：%s'%self.speed_per_second
##
##class Mingtu(Car):
##            def __init__(self):
##                        self.speed_per_second = '210km/s'
##            def __str__(self):
##                        return '最大速度可达：%s'%self.speed_per_second
##
##class Baoma(Car):
##            def __init__(self):
##                        self.speed_per_second = '250km/s'
##            def __str__(self):
##                        return '最大速度可达：%s'%self.speed_per_second
##
##def select_car_type(type):
##            if type == '索纳塔':
##                        return Suonata()
##            elif type == '名图':
##                        return Mingtu()
##            elif type == '宝马':
##                        return Baoma()
##           
##order_type = raw_input("购买车型：")
##
##car_store = CarStore()
##car = car_store.order(order_type)
##print(car)              ##for test


##设计模式
##简单工厂模式:使用类来解耦
class CarStore(object):
            def __init__(self):
                        self.select= SelectCar()
            
            def order(self,type):
                        return self.select.select_car_type(type)

class Car(object):
            def move():
                        print('---run---')
            def music():
                        print('---play music---')
            def stop():
                        print('---stop---')

class Suonata(Car):
            def __init__(self):
                        self.speed_per_second = '180km/s'
            def __str__(self):
                        return '最大速度可达：%s'%self.speed_per_second

class Mingtu(Car):
            def __init__(self):
                        self.speed_per_second = '210km/s'
            def __str__(self):
                        return '最大速度可达：%s'%self.speed_per_second

class Baoma(Car):
            def __init__(self):
                        self.speed_per_second = '250km/s'
            def __str__(self):
                        return '最大速度可达：%s'%self.speed_per_second
class SelectCar(object):
            def select_car_type(self,type):
                        if type == '索纳塔':
                                    return Suonata()
                        elif type == '名图':
                                    return Mingtu()
                        elif type == '宝马':
                                    return Baoma()
           
order_type = input("购买车型：")

car_store = CarStore()
car = car_store.order(order_type)
print(car)              ##for test






































