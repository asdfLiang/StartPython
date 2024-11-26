import logging

"""
    日志格式化输出
"""

# logging.basicConfig(
#     format="日志级别: %(levelname)s\n 日志内容: %(message)s", level=logging.DEBUG
# )

logging.basicConfig(
    format="日志时间: %(asctime)s \n 日志内容: %(message)s", level=logging.DEBUG
)

# 创建exam.log文件，并设置级别
logging.info("================================================")
# 写入debug信息
logging.debug("this is a debug")
# 写入info信息
logging.info("this is a info")
# 写入warning信息
logging.warning("this is a warning")
