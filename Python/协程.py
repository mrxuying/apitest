def test1():
            while True:
                        print('---1---')
                        yield None

def test2():
            while True:
                        print('---2---')
                        yield None

thread1 = test1()
thread2 = test2()
while True:
            thread1.__next__()
            thread2.__next__()

            
