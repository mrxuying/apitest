from multiprocessing import Process
import time
##这样创建的子进程可以跨平台运行
def test():
            for i in range(5):
                        print('---test---')
                        time.sleep(1)

p = Process(target = (test(),))
p.start()   ##子进程开始执行test

for i in range(5):
            print('---main---')
            time.sleep(1)
