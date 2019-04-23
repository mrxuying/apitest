##class Num(object):
##            def __init__(self):
##                        self.__num = 100
##
##            @property
##            def num(self):
##
##                        print('-----getter------')
##                        return self.__num
##
##            @num.setter
##            def num(self,new_num):
##
##                        print('-----setter------')
##                        self.__num = new_num
##
##test = Num()
##
##test.num +=  200
##print(test.num)
##
##print('-'*50)
##
##sample = Num()
##sample.num = 888
##print(sample.num)


class Num(object):
            def __init__(self):
                        self.__num = 100


            def setNum(self):

                        print('-----getter------')
                        return self.__num


            def getNum(self,new_num):

                        print('-----setter------')
                        self.__num = new_num

            num = property(setNum, getNum)

test = Num()
test.num +=  200
print(test.num)

print('-'*50)

sample = Num()
sample.num = 888
print(sample.num)




            
