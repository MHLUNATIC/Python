# http://www.cnblogs.com/alex3714/articles/5161349.html
# Python 使用logging模块记录日志涉及四个主要类，使用官方文档中的概括最为合适：
# logger提供了应用程序可以直接使用的接口；
# handler将(logger创建的)日志记录发送到合适的目的输出；
# filter提供了细度设备来决定输出哪条日志记录；
# formatter决定日志记录的最终输出格式。

# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message') #默认级别
# logging.error('error message')
# logging.critical('critical message')

import logging
logger = logging.getLogger()# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
