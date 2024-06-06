# -*- coding: utf-8 -*-

"""
这是当前项目|业务的公共测试用例基类
该类继承最外层的公共测试用例基类BaseTestClass
为测试用例基类提供业务上的初始化|setup|teardown等功能

Attributes:

Functions:
    None

Classes:
    BaseTestCase:
        继承自公共的BaseTestClass，为当前测试用例基类提前注册user_actions|setup|teardown

"""

import os
import json
import pandas as pd
from loguru import logger
from conftest import RootPath
from test_collections.basetestcase import BaseTestClass
from test_collections.suites_project_a.action_collection.user_actions import UserActions


def init_test_data():
    """
    初始化测试数据
    :return:
    """

    # 定义一个函数来解析JSON字符串，处理错误
    def parse_json(x):
        try:
            return json.loads(x) if isinstance(x, str) and x.strip() else x
        except json.JSONDecodeError:
            logger.info(f"Error decoding JSON for value: {x}")
            return x  # 如果解码失败，返回原始值

    def list_to_dict(lst):
        return {str(i["CaseId"]): i for i in lst}

    # 拼装excel路径
    case_data_file = os.path.join(
        RootPath, "test_collections", "suites_project_a", "case_data", "checklist_case_data.xlsx")
    # 使用pandas的ExcelFile类读取Excel文件，但不立即加载数据
    xls = pd.ExcelFile(case_data_file)
    # 获取所有sheet的名称
    sheet_names = xls.sheet_names
    # 创建一个字典来存储所有的DataFrame
    dfs = dict()
    # 遍历所有的sheet页
    for sheet_name in sheet_names:
        # 读取每个sheet页的数据到DataFrame
        df = pd.read_excel(case_data_file, engine="openpyxl", sheet_name=sheet_name)
        # 填充空单元格数据为空字符串
        df.fillna("")
        # 检查是否有'Params'列, 有就将其整列从json字符串转换成字典
        if "TestData" in df.columns:
            # 使用apply函数将'Params'列中的JSON字符串转换为字典
            df['TestData'] = df['TestData'].apply(parse_json)

        if sheet_name == "CaseData":
            dfs[sheet_name] = list_to_dict(df.to_dict(orient='records'))
        else:
            # 将DataFrame以sheet的名称作为键存储到字典中
            dfs[sheet_name] = df.to_dict(orient='records')

    return dfs


class BaseTestCase(BaseTestClass):
    ChecklistCaseData = init_test_data()

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.logger.info(cls.ChecklistCaseData)  # 测试开始时读取一次测试数据即可

    @classmethod
    def setup_method(cls):
        super().setup_class()
        # 用例开始时初始化一次登录
        cls.user_actions = UserActions(
            api_host=cls.ChecklistCaseData["EnvInfo"][0]["ApiHost"],
            locator_host=cls.ChecklistCaseData["EnvInfo"][0]["LocatorHost"],
            username=cls.ChecklistCaseData["EnvInfo"][0]["Username"],
            password=cls.ChecklistCaseData["EnvInfo"][0]["Password"],
            user_id=cls.ChecklistCaseData["EnvInfo"][0]["Userid"],
        )
