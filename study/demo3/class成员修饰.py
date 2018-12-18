# 成员修饰符：
# 共有成员
# 私有成员：__字段名  外部无法直接访问，只能间接访问(通过同一个类内部）
class Qoo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__age = age
obj = Qoo('ds','23')
obj.name
obj.age
# obj.__age  #外部无法直接访问 AttributeError: 'Qoo' object has no attribute '__age'

# 特殊成员
# __init__  类()自动执行
# __del__   '析构方法':对象被销毁时，自动执行
# __call__ 对象() 类()() 自动执行
# __int__ int(对象) 自动执行对象的 __int__ 方法，并将返回值赋值给int对象
# __str__   如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。
#
# __add__  两个对象相加时（+），自动执行第一个对象的的 __add__ 方法，并且将第二个对象当作参数传递进入
# __dict__  对象.__dict__ :讲对象中封装的所有内容通过字典的形式返回
# __getitem__  切片（slice类型）或者索引
# __setitem__
# __delitem__
class Foo:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __getitem__(self, item):
        # return item+10
        # 如果item是基本类型：int，str，索引获取
        # slice对象的话，切片
        if type(item) == slice:
            print('调用这希望内部做切片处理')
            print(item.start)
            print(item.stop)
            print(item.step)
        else:
            print('调用这希望内部做索引处理')
    def __setitem__(self, key, value):
        print(key,value)
    def __delitem__(self, key):
        print(key)
li = Foo('alex', 18)
li[123]            #对应__getitem__
li[1:4:2]          #对应__getitem__
li[1:3] = [11,22]  #对应__setitem__
del li[1:3]        #对应__delitem__
#
# __iter__
# 如果类中有 __iter__ 方法，对象=》可迭代对象
# 对象.__iter__() 的返回值： 迭代器
# for 循环迭代器，next
# for 循环可迭代对象，执行 对象.__iter__() 获取返回值(迭代器)，next
class Foo:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __iter__(self):
        return iter([11,22,33])
li = Foo('alex', 18)
for i in li:
    print(i)