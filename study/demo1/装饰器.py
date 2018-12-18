# 软件开发中的一个原则“开放-封闭”原则，简单来说，它规定已经实现的功能代码不允许被修改，但可以被扩展，即：
# 封闭：已实现的功能代码块不应该被修改
# 开放：对现有功能的扩展开放

#Python内置的@property装饰器就是负责把一个方法变成属性调用的

import time

def time_logger(flag=0):
    def show_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('spend %s' % (end_time - start_time))

            if flag:
                print('将这个操作的时间记录到日志中')

        return wrapper

    return show_time

@time_logger(3)  #@show_time等于add=show_time(add)
def add(*args, **kwargs):
    time.sleep(1)
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(3, 7, 5)