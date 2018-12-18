# python中的反射功能是由以下四个内置函数提供：hasattr、getattr、setattr、delattr，
# 四个函数分别用于对对象内部执行：检查是否含有某成员、获取成员、设置成员、删除成员。
#反射是通过字符串的形式操作对象相关的成员。一切事物都是对象
class Foo:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show(self):
        return  "%s-%s " %(self.name,self.age)
obj = Foo('alex', 18)
b = 'name'  #  getattr(obj, b)通过b实现调用self.name
# inp = input('>>>')
# v = getattr(obj, inp )     # 去什么东西里面获取什么内容
# print(v)
func = getattr(obj, 'show')
print(func)
r = func()
print(r)
print(hasattr(obj, 'name'))
# obj.k1
# setattr(obj, 'k1', 'v1')
# print(obj.k1)
# obj.name
# delattr(obj, 'name')
# obj.name

