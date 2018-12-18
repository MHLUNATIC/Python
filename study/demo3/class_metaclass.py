# obj对象是通过执行Foo类的构造方法创建，Foo类对象 是通过type类的构造方法创建
# obj对象是Foo类的一个实例，Foo类对象是 type 类的一个实例
# 创建类就可以有两种方式:普通方式
class Foo(object):
    def func(self):
        print('hello wupeiqi')
# 特殊方式(type类的构造函数):type第一个参数：类名,第二个参数：当前类的基类,第三个参数：类的成员
def dfunc(self):
    print('hello wupeiqi')
Foo = type('Foo', (object,), {'func': dfunc})
#类中有一个属性 __metaclass__，其用来表示该类由谁来实例化创建，
# 所以我们可以为 __metaclass__ 设置一个type类的派生类，从而查看类创建的过程
class MyType(type):
    def __init__(self,*args, **kwargs):
        # self=Foo
        print(123)
        pass
    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj)
class Foo(object,metaclass=MyType):
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)
    def func(self):
        print('hello wupeiqi')
obj = Foo()
# 第一阶段：解释器从上到下执行代码创建Foo类,执行MyType中的__init__
# 第二阶段：通过Foo类创建obj对象，执行MyType中的__call__调用执行Foo中__new__创建对象obj，执行Foo中 __init__
