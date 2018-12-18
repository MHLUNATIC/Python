#线程是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位 。
#一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务
# GIL(Global Interpreter Lock)是在实现Python解析器(CPython)时所引入的一个概念
# GIL作用：同一时刻允许一个线程执行操作
# 解决多线程问题：使用多进程，协程
# 进程之间相互独立，同一进程里线程之间可以通信（交换，共享数据）
# 在python里如果任务是IO密集型(IO阻塞状态)的可以用多线程，是计算密集型的最好改用C语言解决
# 线程的2种调用方式：直接调用，继承（类）
# import threading        方法一
# t1 = threading.Thread(target=类或方法, args=(参数,))  # 生成一个线程实例
# t1.start()  # 启动线程
import threading         #方法二
import time
class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):  # 定义每个线程要运行的函数

        print("running on number:%s" % self.num)
        time.sleep(3)
if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.setDaemon(True)
    t2.start()
    t1.join()
# setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置。这个方法基本和join是相反的。
# 但是有时候我们需要的是只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以用setDaemon方法啦
#  t.join()：在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
#Timer(定时器):指定n秒后执行某操作
from threading import Timer
def hello():
    print("hello, world")
t = Timer(1, hello)
t.start()  # after 1 seconds, "hello, world" will be printed

