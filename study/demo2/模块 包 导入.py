# 一个.py文件就称之为一个模块（Module）。模块一共三种：python标准库，第三方模块，应用程序自定义模块
# import random                          通过搜索路径找到random.py，将random = random.py所有代码
# from random import randrange,randint  从模块调用方法，只加载了randrange,randint
# from random import *                  不使用这种方法
# Python又引入了按目录来组织模块的方法，称为包（Package）
# import 包    执行的是包下的 __init__.py        导入一个包，解释器解释该包下的 __init__.py 文件
# from 包.包 import 模块                                      导入一个py文件，解释器解释该py文件
# from 包.包.模块 import 方法
print(__file__)  #当前想对路径
#要用import导入的包不在当前目录下，找到最上层路径加到回京变量中
import sys
import os
# 用os.path.abspath()把相对路径变成绝对路径,用os.path.dirname()找到目标路径F:\Python.py\PycharmProjects\study
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR) #将目标路径加到环境变量
#__name__在所在模块中执行是__main__，__name__在被调用的文件中执行是所在模块的文件名
print(__name__)
if __name__ == '__main__':
    pass  #测试代码
