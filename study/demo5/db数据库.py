# MySQL是一个关系型数据库管理系统，在WEB应用方面MySQL是最好的RDBMS(Relational Database Management System，
# 关系数据库管理系统) 应用软件之一。
# Window版本：初始化时使用的【mysqld --initialize-insecure】命令，其默认未给root账户设置密码
# 1、下载 2、解压 3、初始化 4、启动MySQL服务 5、启动MySQL客户端并连接MySQL服务
# 为使用时操作简便：a.将路径添加环境变量 b.将MySQL服务制作成windows服务
# 因为在执行【mysqd】启动MySQL服务器时，当前终端会被hang住，所以将其制作成windows服务
# 制作MySQL的Windows服务，在终端执行此命令："c:\mysql-5.7.16-winx64\bin\mysqld" - -install
# 移除MySQL的Windows服务，在终端执行此命令："c:\mysql-5.7.16-winx64\bin\mysqld" - -remove
# 注册成服务之后 启动MySQL服务：net start mysql  关闭MySQL服务：net stop mysql
# Linux版本：    安装：yum install mysql-server　
# 服务端启动：mysql.server start  客户端连接：mysql - h host - u user - p  退出：QUIT或者Control + D
#
# 据库操作:
# show databases;  # 查看当前Mysql都有那些数据，根目录都有那些文件夹
# create database 数据库名称 default charset utf8 collate utf8_general_ci;     #创建数据库(创建文件夹)
# use 数据库名;  使用选中数据库，进入目录         显示当前使用的数据库中所有表：show tables;
#
# 用户管理：
# 创建用户:create user '用户名'@'IP地址' identified by '密码';
# 删除用户:drop user '用户名'@'IP地址';
# 修改用户:rename user '用户名'@'IP地址'; to '新用户名'@'IP地址';;
# 修改密码:set password for '用户名'@'IP地址' = Password('新密码')
#
# 授权管理：
# show grants for '用户'@'IP地址' - - 查看权限
# grant 权限 on 数据库.表 to '用户' @ 'IP地址' - - 授权
# revoke 权限 on 数据库.表 from '用户' @ 'IP地址' - - 取消权限

import pymysql
conn = pymysql.connect(host='192.168.31.195', port=3306, user='abc', passwd='123', db='test',charset='utf8')
cursor=conn.cursor()
cursor.execute('insert into class(caption) values("回家的")')
conn.commit()
cursor.close()
conn.close()

#    权限：   all privileges          除grant外的所有权限
#             select                  仅查权限
#             select,insert           查和插入权限
#             ...
#             usage                   无访问权限
#             alter                   使用alter table
#             alter routine           使用alter procedure和drop procedure
#             create                  使用create table
#             create routine          使用create procedure
#             create temporary tables 使用create temporary tables
#             create user             使用create user、drop user、rename user和revoke  all privileges
#             create view             使用create view
#             delete                  使用delete
#             drop                    使用drop table
#             execute                 使用call和存储过程
#             file                    使用select into outfile 和 load data infile
#             grant option            使用grant 和 revoke
#             index                   使用index
#             insert                  使用insert
#             lock tables             使用lock table
#             process                 使用show full processlist
#             select                  使用select
#             show databases          使用show databases
#             show view               使用show view
#             update                  使用update
#             reload                  使用flush
#             shutdown                使用mysqladmin shutdown(关闭MySQL)
#             super                   􏱂􏰈使用change master、kill、logs、purge、master和set global。还允许mysqladmin􏵗􏵘􏲊􏲋调试登陆
#             replication client      服务器位置的访问
#             replication slave       由复制从属使用
#
# 对于目标数据库以及内部其他：
#             数据库名.*            数据库中的所有
#             数据库名.表           指定数据库中的某张表
#             数据库名.存储过程     指定数据库中的存储过程
#             *.*                   所有数据库
#             用户名@IP地址         用户只能在改IP下才能访问
#             用户名@192.168.1.%   用户只能在改IP段下才能访问(通配符%表示任意)
#             用户名@%             用户可以再任意IP下访问(默认IP地址为%)
# flush privileges，将数据读取到内存中，从而立即生效。
# 启动免授权服务端
# mysqld --skip-grant-tables
# 客户端
# mysql -u root -p
# 修改用户名密码
# update mysql.user set authentication_string=password('666') where user='root';
# flush privileges;

