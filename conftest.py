# -*- coding: utf-8 -*-

"""
这是全局项目|业务的 conftest
该类为所有项目提供各种公共fixture
注意：请不要删除下方 find_root_path 方法和 设置logger步骤里面的print和log

"""

import os
import sys
import shutil
from datetime import datetime
from loguru import logger

ProjectName = "automatic_design"


def find_root_path():
    current_dir = os.path.dirname(os.path.realpath(__file__))  # 获取当前目录
    logger.debug(current_dir)
    project_name = ProjectName
    while True:
        # 检查当前目录下是否有requirement.txt文件
        if os.path.exists(os.path.join(current_dir, 'requirement.txt')):
            logger.debug(current_dir)
            print(current_dir)
            return current_dir  # 如果找到，返回当前目录作为项目根目录

        # 如果没有找到，检查当前目录名称是否和指定的项目名称相同
        if os.path.basename(current_dir) == project_name:
            logger.debug(current_dir)
            print(current_dir)
            return current_dir  # 如果相同，返回当前目录作为项目根目录

        # 如果以上两个条件都不满足，则往上一级目录继续查找
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # 防止无限循环，当到达文件系统根目录时停止
            raise ValueError(f"Unable to find project root for '{project_name}'. Reached file system root.")
        current_dir = parent_dir


# --------------- start：开始设置全局logger --------------- #
logger.remove()
# 获取项目根目录，拼接测试报告目录
RootPath = find_root_path()  # 获取当前目录
ReportsDir = os.path.join(RootPath, "reports")
logger.debug(ReportsDir)  # 不要注释或删除

# 获取当前时间，并格式化为字符串，用作本次测试报告文件夹名称
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
ReportDir = os.path.join(ReportsDir, current_time)  # 本次测试报告的存放目录(包含run.log和allure_report目录)
logger.debug(ReportDir)  # 不要注释或删除
AllureReportDir = os.path.join(ReportDir, "allure_report")  # 本次测试报告的存放目录下的allure_report目录)
TmpAllureReportDir = os.path.join(os.getcwd(), "allure_json_report")  # 本次allure-json测试报告的临时存放目录

# 如果目录不存在，则创建它
if not os.path.exists(ReportDir):
    logger.debug(f"create {ReportDir}")
    print(f"create {ReportDir}")
    os.mkdir(ReportDir)
else:
    logger.debug(f"not create {ReportDir}")
    print(f"not create {ReportDir}")

# --------------- start：开始设置全局logger --------------- #
logger.configure(
    handlers=[
        {  # 第一个 handler：输出到控制台
            "sink": sys.stderr,  # 输出到标准错误流
            "level": "DEBUG",  # 输出 DEBUG 级别及以上的日志
            "format": "{time:HH:mm:ss.SSS}  [{level}]  {message}",  # 日志格式
            "enqueue": True,  # 异步写入
            "colorize": True,  # 彩色输出
        },
        {  # 第二个 handler：输出到文件
            "sink": os.path.join(ReportDir, "runcase.log"),  # 输出到当次测试报告文件夹下的文件 "runcase.log"
            # "sink": "pytest.log",  # 输出到当次测试报告文件夹下的文件 "test.log"
            "level": "DEBUG",  # 输出 DEBUG 级别及以上的日志
            "format": "{time:HH:mm:ss.SSS}  [{level}]  {message}",  # 日志格式
            "encoding": "utf-8",  # 编码
            "rotation": "10 MB",  # 文件大小达到 10 MB 时进行日志轮转
            # "retention": "10 days",  # 保留最近 10 天的日志
            # "compression": "zip",  # 压缩旧日志文件为 zip 格式
            "enqueue": True,  # 异步写入
        },
    ]
)


# --------------- end：结束设置全局logger --------------- #
def pytest_sessionfinish(session, exitstatus):
    # 通过当前的 allure json 测试报告目录，生成 allure html 测试报告
    os.system(f"allure generate {TmpAllureReportDir} -o {AllureReportDir} --clean")
    # 将 allure json 测试报告目录复制到 当前 allure_report 测试报告目录下
    shutil.copytree(TmpAllureReportDir, os.path.join(AllureReportDir, "json_report"))
    # 删除 allure json 测试报告临时目录
    shutil.rmtree(TmpAllureReportDir)
