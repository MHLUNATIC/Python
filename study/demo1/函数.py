# 函数在BASIC中叫做subroutine(子过程或子程序)，在Pascal中叫做procedure(过程)和function，在C中只
# 有function，在Java里面叫做method。
# 定义: 函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可
# 特性:1. 减少重复代码 2.使程序变的可扩展 3.使程序变得易维护

# 形参：形式参数，不是实际存在，是虚拟变量。在定义函数和函数体的时候使用形参，目的是在函数调用时接收
#       实参（实参个数，类型应与实参一一对应）
# 实参：实际参数，调用函数时传给函数的参数，可以是常量，变量，表达式，函数，传给形参
# 参数:1.必备参数 2.关键字参数 3.默认参数(缺省参数) 4.不定长参数:加了星号（*）的变量名会存放所有未
#       命名的变量参数。而加(**)的变量名会存放命名的变量参数       (*args)  (**kargs)

# 返回值return
# 高阶函数是至少满足下列一个条件的函数:1.接受一个或多个函数作为输入 2.输出一个函数

#作用域：搜索变量的优先级顺序依次是：LEGB,作用域局部>外层作用域>当前模块中的全局>python内置作用域。
#  L：local，局部作用域，即函数中定义的变量；
# E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
# G：globa，全局变量，就是模块级别定义的变量；
# B：built-in，系统固定模块里面的变量，比如int, bytearray等。
# 在Python中，只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域
# 当内部作用域想修改外部作用域的变量时，就要用到global(改全局变量)和nonlocal(改嵌套变量)

def func(n):   #在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
    if n==1:
        return 1
    return n*func(n-1)

def fibo(n):   #斐波那契  0 1 1 2 3 5 8 13 21 ……
    if n==0 or n==1:
        return n
    return fibo(n-1)+fibo(n-2)

# 重要的内置函数：
# 1.filter(function, sequence)
str = ['a', 'b', 'c', 'd']
def fun1(s):
    if s != 'a':
        return s
ret = filter(fun1, str)
print(list(ret))  # ret是一个迭代器对象['b', 'c', 'd']
# 对sequence中的item依次执行function(item)，将执行结果为True的item做成一个filterobject的迭代器返回。可以看作是过滤函数。
# 2.map(function, sequence)
str = ['a', 'b']
def fun2(s):
    return s + "alvin"
ret = map(fun2, str)
print(ret)  # map object的迭代器:<map object at 0x00000229E73D3898>
print(list(ret))  # ['aalvin', 'balvin']
# 对sequence中的item依次执行function(item)，将执行结果组成一个mapobject迭代器返回.
# map也支持多个sequence，这就要求function也支持相应数量的参数输入：
def add(x, y):
    return x + y
print(list(map(add, range(10), range(10))))  ##[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# 3.reduce(function, sequence, starting_value)　　
from functools import reduce
def add1(x, y):
    return x + y
print(reduce(add1, range(1, 101)))  ## 5050
print(reduce(add1, range(1, 101), 20))  ## 5070
# 对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用.
# 4.lambda
# 普通函数
def add(a, b):
    return a + b
print(add(2, 3))
# 匿名函数:因为lamdba在创建时不需要命名
add = lambda a, b: a + b
print(add(2, 3))
# 匿名函数的命名规则，用lamdba 关键字标识，冒号（：）左侧表示函数接收的参数（a,b） ,冒号（：）右侧
#    表示函数的返回值（a+b）。

# Built - in Functions:
# abs()	dict()	help()	min()	setattr()
# all()	dir()	hex()	next()	slice()
# any()	divmod()	id()	object()	sorted()
# ascii()	enumerate()	input()	oct()	staticmethod()
# bin()	eval()	int()	open()	str()
# bool()	exec()	isinstance()	ord()	sum()
# bytearray()	filter()	issubclass()	pow()	super()
# bytes()	float()	iter()	print()	tuple()
# callable()	format()	len()	property()	type()
# chr()	frozenset()	list()	range()	vars()
# classmethod()	getattr()	locals()	repr()	zip()
# compile()	globals()	map()	reversed()	__import__()
# complex()	hasattr()	max()	round()
# delattr()	hash()	memoryview()	set()　　
