# SocketServer模块也是Python标准库中很多服务器框架的基础
# import socketserver
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         逻辑代码块
# if __name__=="__main__":
#     server=socketserver.ThreadingTCPServer(('192.168.31.195',8879),Myserver)
#     server.serve_forever()

import socketserver
import subprocess

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
#######需要自己写的逻辑代码块
        while True:
            try:
                date = conn.recv(1024)
            except Exception:
                break
            if not date: break
            print('....', str(date, 'utf8'))

            obj = subprocess.Popen(date.decode('utf8'), shell=True, stdout=subprocess.PIPE)
            cmd_result = obj.stdout.read()
            result_len = bytes(str(len(cmd_result)), 'utf8')
            print('>>', result_len)
            conn.sendall(result_len)  # 粘包现象:多个
            conn.recv(1024)  # 解决粘包现象
            conn.sendall(cmd_result)
        conn.close()
if __name__=="__main__":
    server=socketserver.ThreadingTCPServer(('192.168.31.195',8879),Myserver)
    server.serve_forever()

