# 迭代器满足迭代器协议两个条件:内部有iter方法，内部有next方法
# 生成器都是迭代器
# 可迭代对象：tuple,list,dict,string

l=[1,1,3,4,5,6,7]
d=iter(l)
print(d)
# for 循环内部三件事
#     1.调用可迭代对象的iter方法返回一个迭代器对象
#     2.不断调用迭代器对象的next方法
#     3.处理StopIteration异常