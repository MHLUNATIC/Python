# 配置文件模块：用于生成和修改常见配置文档，当前模块的名称在 python 3.x 版本中变更为 configparser
# http://www.cnblogs.com/alex3714/articles/5161349.html            configparser增删改查语法

import configparser

config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
# config['bitbucket.org'] = {'User':'hg'}
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

config.read('example.ini')#读取
print(config.sections())#块的信息 不包括default(读取时)
print(config.defaults())#默认项的内容
print(config.default_section)
print(config['bitbucket.org']['User'])

for key in config['topsecret.server.com']:
    print(key)

config.remove_section('topsecret.server.com')
config.has_section('topsecret.server.com')
config.add_section('topsecret.server.com')
config.set('bitbucket.org','user','ere')
config.remove_option('bitbucket.org','user')

config.write(open('i.cfg', "w"))# 改和删必须有