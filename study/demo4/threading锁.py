# 1.lock(同步锁或线程锁或互斥锁Mutex)：当多个线程同时修改同一条数据时，我们只需要把计算(涉及到操作公共数据)的时候串行执行。
# 2.RLock(递归锁)：为了支持在同一线程中多次请求同一资源，python提供了“可重入锁”：threading.RLock。
#   RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次acquire。直到一个线程所有的acquire都被release，其他的线程才能获得资源。
# 3.Semaphore(信号量)：是同时允许一定数量的线程更改数据   常用threading.BoundedSemaphore
# 4.Condition(条件变量):有一类线程需要满足条件之后才能够继续执行，Python提供了threading.Condition对象用于条件变量线程的支持，
# 它除了能提供RLock()或Lock()的方法外，还提供了wait()、notify()、notifyAll()方法。
# lock_con = threading.Condition([Lock / Rlock])： 锁是可选选项，不传锁，对象自动创建一个RLock()。
# wait()：条件不满足时调用，线程会释放锁并进入等待阻塞；notify()：条件创造后调用，通知等待池激活一个线程；
# notifyAll()：条件创造后调用，通知等待池激活所有线程。
# 死锁：（解决死锁的办法是用RLock）在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁，因为系统判断这部分资源都正在使用，所有这两个线程在无外力作用下将一直等待下去。
import threading,time             #Semaphore
class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():    #  .acquire()  获取锁（加锁）
            print(self.name)
            time.sleep(5)
            semaphore.release()    #  .release    释放锁（解锁）
if __name__=="__main__":
    semaphore=threading.BoundedSemaphore(5)
    thrs=[]
    for i in range(100):
        thrs.append(myThread())
    for t in thrs:
        t.start()

import threading,time             #.Condition
from random import randint
class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val=randint(0,100)
            print('生产者',self.name,":Append"+str(val),L)
            if lock_con.acquire():                 #  .acquire()  获取锁（加锁）
                L.append(val)
                lock_con.notify()
                lock_con.release()                 #  .release    释放锁（解锁）
            time.sleep(3)
class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
                lock_con.acquire()
                if len(L)==0:
                    lock_con.wait()
                print('消费者',self.name,":Delete"+str(L[0]),L)
                del L[0]
                lock_con.release()
                time.sleep(0.25)

if __name__=="__main__":

    L=[]
    lock_con=threading.Condition()
    threads=[]
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()