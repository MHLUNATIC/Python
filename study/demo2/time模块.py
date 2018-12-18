# 时间有三种表示方式：
#     时间戳                          1970年1月1日之后的秒，即：time.time()
#     格式化的字符串                  2014-11-11 11:11，    即：time.strftime('%Y-%m-%d')
#     结构化时间 (struct_time)        元组包含了：年、日、星期等... time.struct_time    即：time.localtime()
import time
print(time.time())  #时间戳 从1970开始到现在秒数
time.sleep(2)
print(time.clock()) #cpu执行时间
print(time.gmtime())#结构化时间
print(time.localtime())
struct_time=time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time)) #格式化时间
print(time.strptime('2018-05-22 19:21:05','%Y-%m-%d %H:%M:%S'))  #将日期字符串转成 struct时间对象格式
print(time.ctime()) #将时间戳转化格式化时间
print(time.mktime(time.localtime()))#将结构化时间转化成时间戳
print(time.clock()) #返回处理器时间,3.3开始已废弃 , 改成了time.process_time()测量处理器运算时间,不包括sleep时间,不稳定,mac上测不出来
print(time.altzone)  #返回与utc时间的时间差,以秒计算\
print(time.asctime()) #返回时间格式"Fri Aug 19 11:14:16 2016",
print(time.asctime(time.localtime())) #返回时间格式"Fri Aug 19 11:14:16 2016",

import datetime
print(datetime.datetime.now())#返回当前时间  格式为：2016-08-19 12:47:03.941925
# print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2016-08-19
# print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
# print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
# print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
'''
datetime.date：表示日期的类。常用的属性有year, month, day
datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond
datetime.datetime：表示日期时间
datetime.timedelta：表示时间间隔，即两个时间点之间的长度
timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
strftime("%Y-%m-%d")
'''