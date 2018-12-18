# 单例，顾名思义单个实例。单例模式用来保证内存中仅存在一个实例（对象）
class Foo:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        else:
            obj = object.__new__(cls, *args, **kwargs)
            cls.__instance = obj
            return cls.__instance
obj = Foo()
obj1 = Foo()
obj2 = Foo()
obj3 = Foo()
print(obj)
print(obj1)
print(obj2)
print(obj3)

# 另一种写法

# class Foo:
#     __v = None
#     @classmethod
#     def get_instance(cls):
#         if cls.__v:
#             return cls.__v
#         else:
#             cls.__v = Foo()
#             return cls.__v
# obj = Foo.get_instance()
# obj1 =Foo.get_instance()
# obj2 =Foo.get_instance()
# obj3 =Foo.get_instance()
# print(obj)
# print(obj1)
# print(obj2)
# print(obj3)

