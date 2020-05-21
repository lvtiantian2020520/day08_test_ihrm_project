import logging
import os
from logging import handlers

HEADERS = None

EMPID = None
# 定义基础项目路径的变量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1.创建一个初始化日志的函数
def init_logging():
    # 2.在函数中创建日志器
    logger = logging.getLogger()
    # 3.设置日志等级
    logger.setLevel(logging.INFO)
    # 4.创建处理器
    sh = logging.StreamHandler()
    filename = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, when='S', interval=5, backupCount=3, encoding='utf-8')
    # 5.创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 6.将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 7.将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)
    # 8.在api模块下的__init__.py文件中进行初始化
