# 对文件操作流程:1.打开文件，得到文件句柄并赋值给一个变量;2.通过句柄对文件进行操作;3.关闭文件
# f.open('文件名'，'模式(r,w,a)'，encoding="utf8")
# f.read()            f.read(5)读取5个字符      f.readline()   f.readlines()
# f.write("内容")
# f.append("内容")    在原文内容后添加要写入的内容
# f.close()
# f.tell()            查光标位置，默认为0，英文对应一个字符，汉字占三个字符
# f.seek（）          调光标的位置
# f.flush()           将缓存的内容存到磁盘上
# f.truncate(5)       截断 5个字符后的清空

# 打开文件的模式有：
# r，只读模式（默认）。
# w，只写模式。【不可读；不存在则创建；存在则删除内容；】
# a，追加模式。【可读；  不存在则创建；存在则只追加内容；】
# "+" 表示可以同时读写某个文件
# r+，读写模式，写内容写在最后
# w+，写读模式，先写后读，想读到内容先调光标位置
# a+，追加，可读，光标默认在最后（开始时）
# "U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
# rU
# r+U
# "b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
# rb
# wb
# ab

# with语句：为了避免打开文件后忘记关闭，可以通过管理上下文，即：
# with open('log', 'r') as f:
#     pass
# 如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源。
# 在Python 2.7 后，with又支持同时对多个文件的上下文进行管理，即：
# with open('log1') as obj1, open('log2') as obj2:
#     pass
