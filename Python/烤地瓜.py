class SweetPotato:
            '''创建了一个地瓜的类'''
            def __init__(self):
                        ##存储对象属性的方法
                        self.cooked_level = 0
                        self.cookedString = "生的"
            def __str__(self):
                        return "地瓜现在是：%s[%d]"%(self.cookedString,self.cooked_level)
                        ##返回地瓜的属性
            def cook(self,cooked_time):
                        self.cooked_level += cooked_time
                        ##将烤的时间加到烤的程度中
                        if self.cooked_level >=0 and self.cooked_level <3:
                                    self.cookedString = "生的"
                        elif self.cooked_level >=3 and self.cooked_level <5:
                                    self.cookedString = '半生不熟的'
                        elif self.cooked_level >=5 and self.cooked_level <8:
                                    self.cookedString = '熟了'
                        elif self.cooked_level >=8:
                                    self.cookedString = '糊了'
digua = SweetPotato()
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)

