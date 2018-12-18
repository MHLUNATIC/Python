import random
print(random.random()) #0到1的随机数
print(random.randint(1,8))#包括右边8
print(random.choice('hello'))
print(random.choice([1,2,(5,6)]))
print(random.sample(['23',44,[3,4],77],2))#选多个
print(random.randrange(1,6))

# 六位随机字母数字验证码
def yan():
    import random
    code=''
    for i in range(6):
        x=random.choice([str(random.randrange(1,9)),chr(random.randrange(65,90))])#chr（）将数字转换成ASCII码表的内容
        code+=x
    print(code)
yan()
