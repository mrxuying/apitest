# -*- coding: cp936 -*-
####����4s��ͳ���֮��;��������
##class CarStore(object):
##            def order(self,type):
##                        if type == '������':
##                                    return Suonata()
##                        elif type == '��ͼ':
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
##                        return '����ٶȿɴ%s'%self.speed_per_second
##
##class Mingtu(Car):
##            def __init__(self):
##                        self.speed_per_second = '210km/s'
##            def __str__(self):
##                        return '����ٶȿɴ%s'%self.speed_per_second
##           
##order_type = input("�����ͣ�")
##
##car_store = CarStore()
##car = car_store.order(order_type)
##print(car)              ##for test

##����
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
##                        return '����ٶȿɴ%s'%self.speed_per_second
##
##class Mingtu(Car):
##            def __init__(self):
##                        self.speed_per_second = '210km/s'
##            def __str__(self):
##                        return '����ٶȿɴ%s'%self.speed_per_second
##
##class Baoma(Car):
##            def __init__(self):
##                        self.speed_per_second = '250km/s'
##            def __str__(self):
##                        return '����ٶȿɴ%s'%self.speed_per_second
##
##def select_car_type(type):
##            if type == '������':
##                        return Suonata()
##            elif type == '��ͼ':
##                        return Mingtu()
##            elif type == '����':
##                        return Baoma()
##           
##order_type = raw_input("�����ͣ�")
##
##car_store = CarStore()
##car = car_store.order(order_type)
##print(car)              ##for test


##���ģʽ
##�򵥹���ģʽ:ʹ����������
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
                        return '����ٶȿɴ%s'%self.speed_per_second

class Mingtu(Car):
            def __init__(self):
                        self.speed_per_second = '210km/s'
            def __str__(self):
                        return '����ٶȿɴ%s'%self.speed_per_second

class Baoma(Car):
            def __init__(self):
                        self.speed_per_second = '250km/s'
            def __str__(self):
                        return '����ٶȿɴ%s'%self.speed_per_second
class SelectCar(object):
            def select_car_type(self,type):
                        if type == '������':
                                    return Suonata()
                        elif type == '��ͼ':
                                    return Mingtu()
                        elif type == '����':
                                    return Baoma()
           
order_type = input("�����ͣ�")

car_store = CarStore()
car = car_store.order(order_type)
print(car)              ##for test






































