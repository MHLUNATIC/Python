# paramiko是一个用于做远程控制的模块，使用该模块可以对远程服务器进行命令或文件操作，值得一说的是，fabric和
# ansible内部的远程管理就是使用的paramiko来现实。

# 下载安装：pip3 install paramiko      pip安装缺少demos文件不能实时交互   下载源码包

# 执行命令 - 通过用户名和密码连接服务器：
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.108', 22, 'alex', '123')
stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())
ssh.close();

# 执行命令 - 过密钥链接服务器：
import paramiko

private_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('主机名 ', '端口', '用户名', key)

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())
ssh.close()

# 上传或者下载文件 - 通过用户名和密码：
import os,sys
import paramiko

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',password='123')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test.py','/tmp/test.py')
t.close()

import os,sys
import paramiko

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',password='123')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test.py','/tmp/test2.py')
t.close()

# 上传或下载文件 - 通过密钥：
import paramiko

pravie_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pravie_key_path)

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test3.py','/tmp/test3.py')

t.close()

import paramiko

pravie_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pravie_key_path)

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test3.py','/tmp/test4.py')

t.close()
