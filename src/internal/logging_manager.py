import logging

"""
    日志管理器
    
    日志模块组件：
    日志器 Logger    提供应用程序调用的接口
    处理器 Handler   将日志发送到指定的位置
    过滤器 Filter    过滤日志信息
    格式器 Formatter 格式化输出日志
"""

# 1）创建一个logger日志管理器，初始化/实例化对象
logger = logging.getLogger()

# 设置logger级别
logger.setLevel(logging.DEBUG)

# 2）定义处理器
# 在控制台输出，StreamHandler
sh = logging.StreamHandler()
# 达到什么级别在控制台输出
sh.setLevel(logging.DEBUG)

# 写有文件里面，FileHandler文件处理器
fh = logging.FileHandler("logs/ftest.log", encoding="utf-8")
fh.setLevel(logging.WARNING)

# 3）定义日志输出格式
formatter = logging.Formatter(
    "记录时间：%(asctime)s\n日志级别：%(levelname)s\n日志信息：%(message)s\n"
)

# 4）告诉哪些处理器要以上述格式进行输出
sh.setFormatter(formatter)
fh.setFormatter(formatter)

# 5）将控制台处理器sh和文件处理器fh添加到logger的Handler中
logger.addHandler(sh)
logger.addHandler(fh)

# 6）设置每个级别日志的内容
logger.debug("测试中")
logger.info("正常运行")
logger.warning("警告")
logger.error("错误")
logger.critical("严重错误")
