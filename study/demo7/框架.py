# DRP原则:Don't  repeat youself
# 框架(framework):特指为解决一个开放性问题而设计的具有一定约束性的支撑结构
# 对于所有的Web应用，本质上其实就是一个socket服务端，用户的浏览器其实就是一个socket客户端。

# Python内置了一个WSGI服务器，这个模块叫wsgiref，application()函数必须由WSGI服务器来调用
# from wsgiref.simple_server import make_server
# def application(environ,start_response):
#     #通过environ封装一个包含所有请求信息的(字典)对象，start_response一个发送HTTP响应的函数(方便的设置响应头)
#     start_response("200 OK",[("contrnt-Type","text/html")])
#     return [b"<h1>hello,web!</h1>"]
# #封装socket对象以及准备过程（socket,bind,listen）
# httpd=make_server("localhost",8080,application)
# print("serving http on 8000...")
# #开始监听请求
# httpd.serve_forever()

from wsgiref.simple_server import make_server
import time
def current_time(request):
    current_time = time.ctime(time.time())
    f = open('current_time.html',"rb")
    data = f.read()
    data =str(data,'utf8').replace("!current_time!",current_time)
    return [data.encode("utf8")]
def routers():
    urlpatterns = (
        ('/time',current_time),
    )
    return urlpatterns
def application(environ,start_response):
    start_response("200 OK", [("contrnt-Type", "text/html")])
    path = environ["PATH_INFO"]       #获取请求路径（地址，端口，路径）
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ["<h1>404</h1>".encode("utf8")]
httpd = make_server("localhost", 8080, application)
print("serving http on 8000...")
httpd.serve_forever()


# MVC就是把web应用分为模型(Model),控制器(Controller),视图(View)三层
# 模型负责业务对象与数据库的对象(ORM),视图负责与用户的交互(页面)，控制器(C)接受用户的输入调用模型和视图完成用户的请求。
# Django的MTV模式本质上与MVC模式没有什么差别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同，
# Django的MTV分别代表：
#        Model(模型)：负责业务对象与数据库的对象(ORM)
#        Template(模版)：负责如何把页面展示给用户
#        View(视图)：负责业务逻辑，并在适当的时候调用Model和Template
# Django还有一个url分发器，它的作用是将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template
# Controller(MVC)     和    View(MTV)
# View(MVC)           和    Template(MTV)