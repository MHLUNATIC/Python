# 生成器一共两种创建方式：
# 1.（x for i in range（0)）
# 2.yield
# 生成器在创建的时候已经决定了能计算出值的个数，调用next的次数超过这个值就会报错StopIteration
def fib(max):
    a,b,c=0,0,1
    while a<max:
        # print(b)
        x=yield b
        b,c=c,b + c
        a+=1

g=fib(10)
print(g)#<generator object fib at 0x00000260BCE4A2B0>
print(next(g))
print(next(g))

# send可以给yield前的变量赋值 g.send(None)等同于next（g）  第一次send前如果没有next，只能传一个send（None）
print(g.send('djhsd'))