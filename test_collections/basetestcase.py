# -*- coding: utf-8 -*-

"""
这是所有项目|业务的公共测试用例基类
该类为所有子类提供了统一的框架功能，不涉及业务
比如统一注册的logger和step功能

Attributes:

Functions:
    None

Classes:
    BaseTestClass:
        继承自公共的BaseTestClass，为当前测试用例基类提前注册user_actions|setup|teardown

"""

from conftest import logger


class BaseTestClass:
    logger = logger  # 在测试用例基类中定义全局case唯一的logger对象

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass
