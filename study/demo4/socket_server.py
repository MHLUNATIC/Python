################################输入命令让server执行并返回执行结果########################################
# import socket
# import subprocess
#
# ip_port = ('192.168.31.195',8879)
# sk = socket.socket()
# sk.bind(ip_port)
# sk.listen(5)
# print("服务端启动...")
# while True:
#     conn, address = sk.accept()
#     while True:
#         try:
#             date = conn.recv(1024)
#         except Exception:
#             break
#         if not date:break
#         print('....',str(date,'utf8'))
#
#         obj=subprocess.Popen(date.decode('utf8'),shell=True,stdout=subprocess.PIPE)
#         cmd_result=obj.stdout.read()
#         result_len=bytes(str(len(cmd_result)),'utf8')
#         print('>>',result_len)
#         conn.sendall(result_len)  #粘包现象:多个
#         conn.recv(1024)               #解决粘包现象
#         conn.sendall(cmd_result)
#
#     conn.close()
################################上传文件#####################################################################
import socket
import os

ip_port = ('192.168.31.195',8879)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
print("服务端启动...")
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
while True:
    conn,adress=sk.accept()
    while True:
        try:
            date1=conn.recv(1024)
            print(date1)
        except Exception:
            break
        cmd,filename,filesize=str(date1,'utf8').split('|')
        path=os.path.join(BASE_DIR,'sssss',filename)
        filesize=int(filesize)
        has_recevie=0
        while filesize != has_recevie:
            date2=conn.recv(1024)
            with open(path,'ab') as f:
                f.write(date2)
                has_recevie+=len(date2)
conn.close()



