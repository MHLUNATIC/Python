# json，用于字符串 和 python数据类型间进行转换
# pickle，用于python特有的类型 和 python的数据类型间进行转换
# Json模块提供了四个功能：dumps、dump、loads、load
# pickle模块提供了四个功能：dumps、dump、loads、load
import json
dic={'name':'alvin','age':23,'sex':'male'}
with open('json.txt','w') as f:
    # date1=json.dumps(dic)
    # f.write(date1)
    json.dump(dic,f)
import json
with open('json.txt', 'r') as f:
    # date2=f.read()
    # date=json.loads(date2)
    date=json.load(f)
print(date)
#Pickle只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
# import pickle
# def foo():
#     print('ok')
# date1=pickle.dumps(foo())
# with open('pickle.txt','wb') as f:    #注意是w是写入str,wb是写入bytes
#     f.write(date1)
# import pickle
# with open('pickle.txt', 'rb') as f:
#     date2=f.read()
# date=pickle.loads(date2)

# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
# shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;key必须为字符串，而值可以是python所支持的数据类型
import shelve
f = shelve.open(r'shelve.txt')
f['stu1_info']={'name':'alex','age':'18'}
f['stu2_info']={'name':'alvin','age':'20'}
f['school_info']={'website':'oldboyedu.com','city':'beijing'}
f.close()
import shelve
f = shelve.open(r'shelve.txt')
print(f.get('stu1_info')['name'])