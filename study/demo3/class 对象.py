# 面向对象编程(Object Oriented Programming，OOP)三大特性是指：封装、继承和多态。
# class是关键字，表示类，类中的函数第一个参数必须是self,self是指调用方法的调用者（对象）
# 领域建模的三字经方法:找名词、加属性、连关系
class Goo:  #父类（基类）
    def ee(self,ty):
        print(ty)
    def ff(self):
        print('G.iu')
class Foo(Goo):  #子类（派生类）:Python中支持多继承:a.左侧优先(广度) b.一条道走到黑(深度) c.同一个根时，根最后执行
    country = '中国'    # 静态字段，属于类
    def __init__(self, name, age): # __init__()叫做初始化方法(或构造方法),用于封装
        #构造方法的特性， 类名()自动执行构造方法
        self.name = name    #普通字段，属于对象
        self.age = age      #普通字段，属于对象
    def uu(self,kj):        #方法
        print(self.name,self.age,kj)
    def ff(self):  #不继承父类的方法就要重新写
        print('F.yy')
        super(Foo, self).ff() #1.主动调用执行父类中的方法（推荐使用）
        # Goo.ff(self)          #2.主动调用执行父类中的方法

obj1 = Foo('ui',67)   # 创建对象，类名称后加括号即可
obj1.uu('df')         #对象调用方法
obj1.ff()




