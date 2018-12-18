# 用于加密相关的操作，代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
import hashlib
m=hashlib.md5() #常用md5算法
print(m)
m.update('hello woeld'.encode('utf8'))
print(m.hexdigest())
m.update('sjhd'.encode('utf8')) #相当于'hello woeldsjhd'
print(m.hexdigest())
m1=hashlib.md5()
m1.update('hello woeldsjhd'.encode('utf8'))
print(m1.hexdigest())

s=hashlib.sha256() #常用
s.update('hello woeld'.encode('utf8'))
print(s.hexdigest())

# python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 再进行处理然后再加密
import hmac
h = hmac.new('wueiqi')
h.update('hellowo')
print(h.hexdigest())

