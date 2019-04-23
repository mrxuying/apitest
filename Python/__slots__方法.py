class Person(object):
            __slots__ = ('name','age')
            def __init__(self):
                        self.sex = 'xy'


p = Person()
p.sex = 'xx'
print(p.sex)
