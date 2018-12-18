def fun():
    ret = 0
    try:
        li = [11, 22]
        li[3232]
    except IndexError as e:    #try内代码块如果出错，自动执行except块的内容
        print('IndexError',e)
    except ValueError as e:
        print('ValueError',e)
    except Exception as e:     # e是Exception对象，对象中封装了错误信息上述代码块如果出错，自动执行当前块的内容
        print('Exception',e)
    else:                      #try内代码块如果没出错执行else
        ret = 1
        print('elese')
    finally:                   #出不出错都要执行
        print('....')
    return ret
r = fun()
if r == 0:
    print('500')
else:
    pass
# 主动触发异常：raise Exception('我错cuo了...')
# 创建自定义异常：
class OldBoyError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
    # obj = OldBoyError('xxx')
    # print(obj)
try:
    raise OldBoyError('我错了...')    #主动触发异常
except OldBoyError as e:
    print(e)  # e对象的__str__()方法，获取返回
 # 断言：assert 条件,用于强制用户服从，不服从就报错，可捕获，一般不捕获
# assert 1==2
# print(456)

# 异常种类：
# AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
# IOError 输入/输出异常；基本上是无法打开文件
# ImportError 无法引入模块或包；基本上是路径问题或名称错误
# IndentationError 语法错误（的子类） ；代码没有正确对齐
# IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError 试图访问字典里不存在的键
# KeyboardInterrupt Ctrl+C被按下
# NameError 使用一个还未被赋予对象的变量
# SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
# TypeError 传入对象类型与要求的不符合
# UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
# ValueError 传入一个调用者不期望的值，即使值的类型是正确的
# ArithmeticError
# AssertionError
# AttributeError
# BaseException
# BufferError
# BytesWarning
# DeprecationWarning
# EnvironmentError
# EOFError
# Exception
# FloatingPointError
# FutureWarning
# GeneratorExit
# ImportError
# ImportWarning
# IndentationError
# IndexError
# IOError
# KeyboardInterrupt
# KeyError
# LookupError
# MemoryError
# NameError
# NotImplementedError
# OSError
# OverflowError
# PendingDeprecationWarning
# ReferenceError
# RuntimeError
# RuntimeWarning
# StandardError
# StopIteration
# SyntaxError
# SyntaxWarning
# SystemError
# SystemExit
# TabError
# TypeError
# UnboundLocalError
# UnicodeDecodeError
# UnicodeEncodeError
# UnicodeError
# UnicodeTranslateError
# UnicodeWarning
# UserWarning
# ValueError
# Warning
# ZeroDivisionError