# 字符格式化输出     数据类型：数字，字符串，字节（bytes），布尔值，列表，元组，字典，集合
#   占位符 %s  s = string
#          %d  d = digit 整数
#          %f  f = float 浮点数，约等于小数
#
# 字符编码      ＡＳＳＩＣ　 每一个字符统一都需要8个bit来存储
# 计算机容量    1位 = 1bit
#               8bit = 1byte = 1字节
#               1024bytes = 1kbytes =1KB                1024个字符，小文档 ，几百k可以表示一张图片
#               1024KB = 1Million Bytes = 1MB = 1兆     几万字的文档， 大图片
#               1024MB = 1Gigabytes                     一个清晰的电影，不是高清，高清能达到数10个g
#               1024GB = 1TB
#               1024TB = 1PB
# 编译型 = 全部翻译，再执行  ，翻译=编译  ，c,c++
# 解释型 = 边执行边翻译， python php java c# perl ruby javascript
# Python解释器类型：CPython  IPython  PyPy  Jython  IronPython
#
# Python 2.6 - October 1, 2008
# Python 2.6.1 - October 1, 2008
# Python 2.6.6 - October 1, 2008
# Python 3.0 - December 3, 2008   支持中文 utf-8
# Python 2.7 - July 3, 2010
# 目前业内主流使用的工业版本依然是2.7 默认编码是ASSIC不支持中文
# 系统位数    32bit = 内存的最大寻址空间是2 ** 32， 4GB
#             64bit, = 2 ** 64但实际上支持不到这莫大的内存，2 ** 4x, 目前主板支持的最大的内存是100多GB
#
# 表达式就是由操作数和运算符组成的一句代码或语句
# 特殊注释：shebang(工作; 事情; 陋屋; 住所;)     #！/user/bin/env  python   注释我为什么这么做
#
#  变量：是为了存储程序运算过程中的一些中间结果，为了方便日后调用，操作或更改
#  常量：固定不变的量，在py里面所有的变量都是可变的 ,所以用全部大写的变量名来代表此变量为常量
#  变量的命名规则
# 	1. 要具有描述性
# 	2. 变量名只能_,数字，字母组成，不可以是空格或特殊字符(#?<.，￥$*!~)
# 	3. 不能以数字开头
# 	4. 保留字符是不能被使用（关键字内建函数等）
# 	5. 驼峰式命、 下划线分割单词
# 	6. 变量名区分大小写
#
#  关键字：   from keyword import kwlist     print(kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
# 'elif','else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
#  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#
# ord("s")返回ascii码数值   chr(115)返回指定的 ASCII 值字符
# id(x)查x的内存地址  type()查数据类型  =号是赋值符  ==是等于   !=是不等于
# print()其实是默认print(end="\n")  显示在同行用end=""
# 注释   单行注释 用#      CRTL+?
# 	    多行注释用三个单引号或三个双引号 '''被注释的内容'''
# python中声明用中文:#!-*-  coding:utf-8  -*-  或 #coding:utf-8
#
# 无限循环=死循环
# continue 结束本次循环，继续下一次循环
# break    跳出整个当前的循环
#
# 布尔值：True   False
# 短路原则
# 对于and 如果前面的第一个条件为假，那么这个and前后两个条件组成的表达式 的计算结果就一定为假，第二个条件就不会被计算
# 对于or 如果前面的第一个条件为真，那么这个or前后两个条件组成的表达式 的计算结果就一定为真，第二个条件就不会被计算
#
# interpreter   解释器
# syntax        语法
# indentation   缩进
# integer       整数
# string        字符串
# Toolbar       工具栏
# Font            字体
# Template        模板
# invalid         无效的
# counter         计数器
# console         控制台
# location      位置
# untitled     未命名的
# fullstack    全栈
# loop         循环
#
# 字符编码
# 支持中文的第一张表就叫GB2312
# 1980    gb2312  6700 +
# 1995    gbk1.0  20000
# 2000    gb18030 27000
# big5    台湾
# unicode 万国码 支持所有国家和地区的编码2 ** 16 = 65535 = 存一个字符统一占用2个字节
# UTF - 8 = unicode的扩展集，可变长的字符编码集，ascii码中内容用1个字节保存，欧字符2个，东亚字符3个
# Assic -->Gb2312 ->gbk1.0 -->gb18030
# Assic -->unicode -->utf - 8 / utf - 16
# unicode是向下兼容gb2312, gbk
#
# C：各个操作系统的开发语言1973
# C++：C + +是C语言的加强版   ，1983年，贝尔实验室的BjarneStroustrup在C语言基础上推出了C++[1] 。 C++进一步扩充和完善了C语言，是一种面向对象的程序设计语言。
# java：1995 由sun公司开发出来，java虚拟机支持跨平台
# php ：1994, 纯web开发语言， 1994Netscape浏览器诞生了
# python：1989年诞生， 刚开始被做为脚本语言， 开发小任务， 跟linux同年诞生，89，1991, 苏联解体， 1991年正式版本
# C# = c sharpe：C#是微软公司发布的一种面向对象的、运行于.NET Framework之上的高级程序设计语言。并定于在微软职业开发者论坛(PDC)上登台亮相。C#是微软公司研究员Anders Hejlsberg的最新成果。C#看起来与Java有着惊人的相似；它包括了诸如单一继承、接口、与Java几乎同样的语法和编译成中间代码再运行的过程。但是C#与Java有着明显的不同，它借鉴了Delphi的一个特点，与COM（组件对象模型）是直接集成的，而且它是微软公司 .NET windows网络框架的主角。
# ruby ：Ruby， 一种简单快捷的面向对象（面向对象程序设计）脚本语言，在20世纪90年代由日本人松本行弘(YukihiroMatsumoto)开发，遵守GPL协议和RubyLicense。它的灵感与特性来自于Perl、Smalltalk、Eiffel、Ada以及Lisp语言。由Ruby语言本身还发展出了JRuby（Java平台）、IronRuby（.NET平台）等其他平台的Ruby语言替代品。Ruby的作者于1993年2月24日开始编写Ruby，直至1995年12月才正式公开发布于fj（新闻组）。因为Perl发音与6月诞生石pearl（珍珠）相同，因此Ruby以7月诞生石ruby（红宝石）命名。Rubyonrailsweb框架
# perl： Unix平台上开发出来的语言，做文字处理非常强大， 可以写出没人能看懂的代码
# shell： 脚本语言， 简单易学，基于unix, linux, 做一些简单的系统管理任务， 运维人员必学
# scalar：Scala是一门多范式的编程语言，一种类似java的编程语言[1], 大数据开发
# erlang ：是一种通用的面向并发的编程语言，它由瑞典电信设备制造商爱立信，函数式编程
# go === Go语言是谷歌2009发布的第二款开源编程语言。Go语言专门针对多处理器系统应用程序的编程进行了优化，使用Go编译的程序可以媲美C或C + +代码的速度，而且更加安全、支持并行进程。
# javascript：是当下使用最为广泛的语言，主要写前端的语言，nodejs = 后端全栈式的语言
# vb：微软的脚本语言，bat脚本
# lua ：nginx的脚本语言， ngnix是时下最nb web服务器
#
# 交互器模式：缺点程序不能永久保存，主要用与简单的语法测试相关
# 开始 - -》cmd --> cd
# c:\  -->dir
# cd = change directory
# dir = 查看当前目录文件列表
# cd ../.. 返回上上一层目录
#
# 数据类型
#     整数
#     字符串
#     列表，元组
#         查
#             索引(下标) ，都是从0开始
#             切片
#             .count 查某个元素的出现次数
#             .index 根据内容找其对应的位置
#             "haidilao ge" in a
#         增加
#             a.append() 追加
#             a.insert(index, "内容")
#             a.extend 扩展
#
#         修改
#             a[index] = "新的值"
#             a[start:end] = [a,b,c]
#
#         删除
#             remove("内容")
#             pop(index)
#             del a, del a[index]
#             a.clear() 清空
#
#         排序
#             sort ()
#             reverse()
#
#         身份判断
#             >>> type(a) is list
#             True
#             >>>