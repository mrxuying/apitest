class Store(object):
            def selec_car(self):
                        pass

            def order(self,type):
                        return self.select_car(type)

class BMWCarStore(Store):
            def select_car(self,type):
                        return BMWFactory().select_car_type(type)

class BMWFactory(object):
            def select_car_type(self,type):
                        if type == 'mini':
                                    return 'red'
                        elif type == 'X6':
                                    return 'black'
                        elif type == '720li':
                                    return 'white'
class NOWCarStore(Store):
            def select_car(self,type):
                        return NOWFactory().select_car_type(type)

class NOWFactory(object):
            def select_car_type(self,type):
                        if type == '名图':
                                    return '1'
                        elif type == '索纳塔':
                                    return '2'
                        elif type == 'ix35':
                                    return '3'

car_type = BMWCarStore()
car = car_type.order('X6')
car_type1 = NOWCarStore()
car1 = car_type1.order('名图')
print (car,car1)
