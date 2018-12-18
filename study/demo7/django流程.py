# django的命令行工具:
# 1.创建一个django工程 : django-admin.py startproject mysite
# mysite  ---- manage.py      (启动文件,Django项目里面的工具，通过它可以调用django shell和数据库等。)
#         ---mysite
#             ---_init_.py
#             ---settings.py  (包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。)
#             ---url.py       (负责把URL模式映射到应用程序。)
#             ---wsgi.py
# 2.在mysite目录下创建blog应用: python manage.py startapp blog
# blog    ---migrations.py
#             ---_init_.py
#         ---_init_.py
#         ---admin.py
#         ---apps.py
#         ---models.py
#         ---test.py
#         ---view.py
# 3.启动django项目：python manage.py runserver 8080    (当我们访问：http://127.0.0.1:8080/时就可以看到)
# 4.生成同步数据库的脚本： python manage.py makemigrations
#             同步数据库:  python manage.py migrate
# 注意：在开发过程中，数据库同步误操作之后，难免会遇到后面不能同步成功的情况，解决这个问题的一个简单粗暴方法是把
# migrations目录下的脚本（除__init__.py之外）全部删掉，再把数据库删掉之后创建一个新的数据库，数据库同步操作再重新做一遍。
# 5.当我们访问http://127.0.0.1:8080/admin/时，会出现：
# 所以我们需要为进入这个项目的后台创建超级管理员：python manage.py createsuperuser，设置好用户名和密码后便可登录啦！
# 6.清空数据库：python manage.py  flush
# 7.查询某个命令的详细信息： django-admin.py  help  startapp     admin 是Django 自带的一个后台数据库管理系统。
# 8.启动交互界面 ：python manage.py  shell
#     这个命令和直接运行 python 进入 shell 的区别是：你可以在这个 shell 里面调用当前项目的 models.py 中的 API，
#     对于操作数据，还有一些小测试非常方便。
# 9.终端上输入python manage.py 可以看到详细的列表，在忘记子名称的时候特别有用。
#

