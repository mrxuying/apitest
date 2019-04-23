from multiprocessing import Pool
import random
import time
import os

def worker(num):
            for i in range(5):
                        print('pid=%d, num = %d'%(os.getpid(),num))
                        time.sleep(1)

pool = Pool(3)          #创建一个数量最大为3的进程池

for i in range(10):
            print('---task%d--'%i)
            pool.apply_async(worker(),(i,))       #让创建的三个进程执行worker


pool.close()            #关闭进程池，停止向进程添加任务；
pool.join()             #让主进程等待子进程执行完成所有任务后再结束；

