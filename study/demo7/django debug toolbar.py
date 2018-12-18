Django调试:

安装：
pip3 install django-debug-toolbar

settings.py 配置:
INSTALLED_APPS 添加   'debug_toolbar',
MIDDLEWARE添加    'debug_toolbar.middleware.DebugToolbarMiddleware',
debug toolbar只会在你设置的IP上显示，这是一个元组，可以添加多个
INTERNAL_IPS = ('127.0.0.1', )
DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL': r"/static/jquery-1.12.4.min.js"}

全局urls.py: 导入 include 和 settings 模块 加上...
from django.conf.urls import url,include
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
四、配置views.py文件
注意：必须要用render返回



