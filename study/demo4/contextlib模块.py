#Python中的上下文管理器(contextlib模块)的任务是：代码块执行前准备，代码块执行后收拾
#自定义上下文管理器:with语句的作用类似于try-finally，提供一种上下文机制。要应用with语句的类，其内部必须提供两个
#内置函数__enter__和__exit__。前者在主体代码执行前执行，后者在主体代码执行后执行。as后面的变量，是在__enter__函数中返回的。

# contextlib模块的作用是提供更易用的上下文管理器，它是通过Generator实现的。contextlib中的contextmanager作为
# 装饰器来提供一种针对函数级别的上下文管理机制，常用框架如下：
from contextlib import contextmanager
@contextmanager
def make_context():
    print('enter')
    try:
        yield "ok"
    except RuntimeError as err:
        print ('error',err)
    finally:
        print('exit')
with make_context() as value:
    print(value)
# 其中，yield写入try-finally中是为了保证异常安全（能处理异常）as后的变量的值是由yield返回。
# yield前面的语句可看作代码块执行前操作，yield之后的操作可以看作在__exit__函数中的操作。
# contextlib.nested:减少嵌套
# with open(filename, mode) as reader:
#     with open(filename1, mode1) as writer:
#         writer.write(reader.read())
# 可以通过contextlib.nested进行简化：
# with contextlib.nested(open(filename,mode),open(filename1,mode1)) as (reader,writer):
#     writer.write(reader.read())
# 在python 2.7及以后，被一种新的语法取代：
# with open(filename,mode) as reader,open(filename1,mode1) as writer:
#     writer.write(reader.read())
# contextlib.closing():file类直接支持上下文管理器API，但有些表示打开句柄的对象并不支持，如urllib.urlopen()返回
# 的对象。还有些遗留类，使用close()方法而不支持上下文管理器API。为了确保关闭句柄，需要使用closing()为它创建一个
# 上下文管理器（调用类的close方法）。
import contextlib
class myclass():
    def __init__(self):
        print('__init__')
    def close(self):
        print('close()')
with contextlib.closing(myclass()):
    print('ok')