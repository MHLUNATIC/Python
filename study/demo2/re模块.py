# 正则表达式：匹配 字符串
# string提供的方法是完全匹配
# 引入正则原因：模糊匹配
import re
ret = re.findall('w\w{2}l','hello world')
print(ret)
# 元字符:  .   ^   $   *   +   ?   {}  []  |   ()  \
#  .（通配符：只能代指任意一个字符，代表除了换行符的所有字符）
ret = re.findall('w..l','hello world')
print(ret)
 # ^(尖角符:在开头开始进行匹配)
ret = re.findall('^h..l','helloasdworld')
print(ret)
# $(在结尾处进行匹配)
ret = re.findall('w...d$','helloasdworld')
print(ret)
# * (匹配*号前的字符0次或多次)
ret = re.findall('w.*d','helloasdworld')
print(ret)
# +(匹配前一个字符1次或多次）
ret = re.findall('w.+d','helloasdworld')
print(ret)
# ?（匹配前一个字符1次或0次）
ret = re.findall('w?o','helloasdworld')
print(ret)
# {}({m}匹配前一个字符m次,{n,m}匹配前一个字符n到m次)
ret = re.findall('w{1,3}o','helloasdwwwwworld')
print(ret)
# [](字符集:范围匹配，取消元字符的特殊功能( \  ^   - 三个除外))^在[]中是取反
ret = re.findall('[a-z]','hecnlloasdxcomwwwwworld')
print(ret)
ret = re.findall('[no]','hecnlloasdxcomwwwwworld')
print(ret)
ret = re.findall('[^o,w]','hecnlloasdxcomwwwwworld')
print(ret)
# \反斜杠后面跟元字符去除特殊功能，反斜杠后面跟普通字符可以实现特殊功能：
# \d  匹配任何十进制数；它相当于类 [0-9]。
# \D 匹配任何非数字字符；它相当于类 [^0-9]。
# \s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
# \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
# \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
# \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
# \b  匹配一个特殊字符边界，比如空格 ，&，＃等
# '\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
# '\Z'    匹配字符结尾，同$
print(re.findall('\d{11}','skjdisj2736721837896545583783wje'))
print(re.findall('\sjd','sk jdisj2736721837896545583783wje'))
print(re.findall('\Sjd','skjdisj2736721837896545583783wje'))
print(re.findall(r'i\b','asdidsdi ds;a'))
# re.search()匹配出第一个满足条件的结果
ret = re.search('o','hecnlloasdorld')
print(ret)
print(ret.group())
ret = re.search('\+','hecnllo+asdorld').group()
print(ret)
ret=re.findall('c\l','abc\le')
print(ret)#[]
ret=re.findall('c\\l','abc\le')
print(ret)#[]
ret=re.findall('c\\\\l','abc\le')
print(ret)#['c\\l']
ret=re.findall(r'c\\l','abc\le')
print(ret)#['c\\l']
# () (分组匹配)
# |(管道符：或)
print(re.search('(as)+','jhasaslaskl').group())
print(re.search('(as)+|3','jh3aslkl').group())# as或3先出现的
ret=re.search('(?P<id>\d{2})/(?P<name>\w{3})','3d23/com')#?p<>是命名
print(ret.group())#23/com
print(ret.group('id'))#23
print(ret.group('name'))
# 正则表达式的方法：
# 1.findall():所有结果都返回到一个列表
# 2.search():返回第一个对象（object），对象可以调用group（）返回结果
# 3.match():只在字符串开始处匹配，也返回第一个对象（object），对象可以调用group（）返回结果
ret=re.match('asd','asd;k;ffe')
print(ret)
print(ret.group())
# 4.split()(以匹配到的字符当做分隔符)
ret=re.split('[k,s]','sdkfsfe')
print(ret)
# 5.sub(替换规则，替换的内容，字符串，替换次数)(匹配字符并替换)
ret=re.sub('d..s','rgfghjddfddfdfyui','sdkfsfe')
print(ret)
ret=re.subn('d..s','rgfghjddfddfdfyui','sdkfsfe')
print(ret)#('srgfghjddfddfdfyuife', 1)   subn显示替换次数
# 注意：前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
ret=re.findall('abc*?','abcccccc')
print(ret)#['ab']
ret=re.findall('www.(\w+).com','www.baidu.com')
print(ret)#['baidu']取到的是组里的内容
ret=re.findall('www.(?:\w+).com','www.baidu.com')
print(ret)#['www.baidu.com'] 涉及优先级问题
ret = re.finditer('\d', 'ds3sy4784a')
print(ret)  # <callable_iterator object at 0x10195f940>
print(next(ret).group())# 3
obj=re.compile('\d{3}')#compile制定匹配规则
ret=obj.search('abc123eeee')
print(ret.group())#123


