#  http://www.cnblogs.com/alex3714/articles/5161349.html

# 如给运行的命令提供输入或者读取命令的输出，判断该命令的运行状态，管理多个命令的并行等等。
# 这时subprocess中的Popen命令就能有效的完成我们需要的操作
# subprocess.Popen(),语法如下:
import subprocess
p = subprocess.Popen("find / -size +1000000 -exec ls -shl {} \;",shell=True,stdout=subprocess.PIPE)
print(p.stdout.read())
# 在创建Popen对象时，subprocess.PIPE可以初始化stdin, stdout或stderr参数。表示与子进程通信的标准流。