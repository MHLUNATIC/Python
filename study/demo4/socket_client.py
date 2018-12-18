################################输入命令让server执行并返回执行结果##TCP######################################
# import socket
# ip_port = ('192.168.31.195',8879)
# sk = socket.socket()
# sk.connect(ip_port)
# print ("客户端启动：")
# while True:
#     inp = input('cdm:>>>').strip( )
#     if len(inp)==0:
#         continue
#     if inp=="q":
#         break
#     sk.sendall(bytes(inp,"utf8"))
#     result_len=int(str(sk.recv(1024),'utf8'))
#     sk.sendall(bytes(111))
#     print(result_len)
#     date=bytes()
#     while len(date)!=result_len:
#         recv=sk.recv(1024)
#         date+=recv
#     print(str(date,'gbk'))
# sk.close()
###################################上传文件##TCP#############################################################
import socket
import os

ip_port = ('192.168.31.195',8879)
sk = socket.socket()
sk.connect(ip_port)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
print ("客户端启动：")
while True:
    inp=input('>>>>').strip()      #输入  post|111.jpg
    cmd,path=inp.split('|')
    path=os.path.join(BASE_DIR,path)
    filename=os.path.basename(path)
    filesize=os.stat(path).st_size
    fileinfo='post|%s|%s'%(filename,filesize)
    sk.sendall(bytes(fileinfo,'utf8'))
    with open(path, 'rb') as f:
        has_send=0
        while has_send!=filesize:
            date2=f.read(1024)
            sk.sendall(date2)
            has_send+=len(date2)
        print('上传成功')
        sk.close()

