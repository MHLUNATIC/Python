# multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。
# 但在使用这些共享API的时候，我们要注意以下几点:
# 1.在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)。所以，有必要
# 对每个Process对象调用join()方法 (实际上等同于wait)。对于多线程来说，由于只有一个进程，所以不存在此必要性。
# 2.multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。应优先考虑Pipe和Queue，避免使用
# Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的不是用户进程的资源)。
# 3.多进程应该避免共享资源。在多线程中，我们可以比较容易地共享资源，比如使用全局变量或者传递参数。在多进程情况下，
# 由于每个进程有自己独立的内存空间，以上方法并不合适。此时我们可以通过共享内存和Manager的方法来共享资源。但这
# 样做提高了程序的复杂度，并因为同步的需要而降低了程序的效率。
# Process.PID中保存有PID，如果进程还没有start()，则PID为None。
# window系统下，需要注意的是要想启动一个子进程，必须加上那句if __name__ == "main"
from multiprocessing import Process
import time
def f(name):
    time.sleep(2)
    print('hello', name)
if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
# 类方法调用：
from multiprocessing import Process
import time
class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
        #self.name = name
    def run(self):
        time.sleep(1)
        print ('hello', self.name,time.ctime())
if __name__ == '__main__':
    p_list=[]
    for i in range(3):
        p = MyProcess()
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()
    print('end')
# 构造方法：
# Process([group [, target [, name [, args [, kwargs]]]]])
# 　　group: 线程组，目前还没有实现，库引用中提示必须是None；
# 　　target: 要执行的方法；
# 　　name: 进程名；
# 　　args/kwargs: 要传入方法的参数。
# 实例方法：
# 　　is_alive()：返回进程是否在运行。
# 　　join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
# 　　start()：进程准备就绪，等待CPU调度
# 　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
# 　　terminate()：不管任务是否完成，立即停止工作进程
# 属性：
# 　　authkey
# 　　daemon：和线程的setDeamon功能一样
# 　　exitcode(进程在运行时为None、如果为–N，表示被信号N结束）
# 　　name：进程名字。
# 　　pid：进程号。  # os.getpid()获取进程号  os.getppid()获取父进程号
import time
from  multiprocessing import Process
def foo(i):
    time.sleep(1)
    print (p.is_alive(),i,p.pid)
    time.sleep(1)
if __name__ == '__main__':
    p_list=[]
    for i in range(10):
        p = Process(target=foo, args=(i,))
        #p.daemon=True
        p_list.append(p)
    for p in p_list:
        p.start()
    # for p in p_list:
    #     p.join()
    print('main process end')
# Queues：
from multiprocessing import Process, Queue
def f(q,n):
    q.put([42, n, 'hello'])
if __name__ == '__main__':
    q = Queue()
    p_list=[]
    for i in range(3):
        p = Process(target=f, args=(q,i))
        p_list.append(p)
        p.start()
    print(q.get())
    print(q.get())
    print(q.get())
    for i in p_list:
            i.join()
# Pipes：
from multiprocessing import Process, Pipe
def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()
# Managers：
from multiprocessing import Process, Manager

def f(d, l,n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l,i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)
# 进程同步：
from multiprocessing import Process, Lock
def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()
if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()
# 进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么
# 程序就会等待，直到进程池中有可用进程为止。进程池中有两个方法：apply，apply_async
from  multiprocessing import Process, Pool
import time
def Foo(i):
    time.sleep(2)
    return i + 100
def Bar(arg):
    print('-->exec done:', arg)
pool = Pool(5)
for i in range(10):
    pool.apply_async(func=Foo, args=(i,), callback=Bar)
    # pool.apply(func=Foo, args=(i,))
print('end')
pool.close()
pool.join()

