# 协程，又称微线程，纤程。英文名Coroutine。一句话说明什么是线程：协程是一种用户态的轻量级线程。
# 线程和进程的操作是由程序触发系统接口，最后的执行者是系统；协程的操作则是程序员。
# 协程存在的意义：对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时（保存状态，下次继续）。
# 协程，则只使用一个线程，在一个线程中规定某个代码块执行顺序。
# 协程的适用场景：当程序中存在大量不需要CPU的操作时（IO），适用于协程；
# 缺点：进行阻塞（Blocking）操作（如IO时）会阻塞掉整个程序
# 使用yield实现协程操作例子:
import time
import queue
def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)
def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()
# greenlet是一个用C实现的协程模块，相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
from greenlet import greenlet
def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()
def test2():
    print(56)
    gr1.switch()
    print(78)
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
# Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet, 它是以C扩
# 展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。
import gevent
def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(2)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')
def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')
gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    # gevent.spawn(func3),
])