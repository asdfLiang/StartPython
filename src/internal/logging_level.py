import logging

"""
    日志

    日志的作用：
        1. 程序调试
        2. 了解软件运行
        3. 软件运行故障与问题定位

    日志等级：
        1. DEBUG    调试信息
        2. INFO     普通信息
        3. WARN     警告信息，发生意向不到的事情，或指示接下来可能会出现的一些问题，但程序还是能够继续运行
        4. ERROR    错误信息，程序运行中已经出现的问题，程序的某些功能不能执行
        5. CRITICAL 危险信息，严重错误，程序无法继续运行

    日志管理器配置步骤：
        1. 初始化对象
        2. 设置级别
        3. 定义handler
        4. 格式化输出
"""

# 创建exam.log文件，并设置级别
logging.basicConfig(filename="logs\exam.log", level=logging.INFO)
logging.info("================================================")
# 写入debug信息
logging.debug("this is a debug")
# 写入info信息
logging.info("this is a info")
# 写入warning信息
logging.warning("this is a warning")
