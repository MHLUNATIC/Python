# 类成员：
# 字段
# - 普通字段，保存在对象中，执行只能通过对象访问
# - 静态字段，保存在类中，  执行 可以通过对象访问 也可以通过类访问
# 方法
# - 普通方法，保存在类中，由对象来调用，self =》对象
# - 静态方法，（加@staticmethod）保存在类中，由类直接调用（类名+方法）,不需要self
# -   类方法，（加@classmethod)保存在类中，由类直接调用，cls =》当前类
# 应用场景：
#         如果对象中需要保存一些值，执行某功能时，需要使用对象中的值　－＞　普通方法
#         不需要任何对象中的值，静态方法
# 特性(属性):(加@property,@per.setter,@per.deleter)定义时是方法，调用时以字段的方式调用
class Foo:
    def __init__(self):
        self.name ='a'
    def bar(self):
        # self是对象
        print('bar')
    @staticmethod
    def stat(a1,a2):
        print(a1,a2)
    @classmethod
    def classmd(cls):
        # cls 是类名
        print(cls)
        print('classmd')
    @property       # 用于执行 obj.per
    def per(self):
        print('112')
        return 1
    @per.setter
    def per(self,val):
        print(val)
    @per.deleter
    def per(self):
        print(666)

obj = Foo()

Foo.bar(obj) #通过类调用方法
Foo.stat(2,2)
Foo.classmd()
r=obj.per
print(r)
obj.per=7657      #对应@per.setter
del obj.per      #对应@per.deleter
# 特性(属性)另一种写法：名字=property(fget=f1,fset=f2,fdel=f3)
class Too:
    def f1(self):
        print('333')
        return 1
    def f2(self,val):
        print(val)
    def f3(self):
        print(555)
    ff=property(fget=f1,fset=f2,fdel=f3) #fget,fset,fdel可以省略
obj1=Too()
obj1.ff
obj1.ff='dsdsd'
del obj1.ff



