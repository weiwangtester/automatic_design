# -*- coding: utf-8 -*-

import pytest
from allure import feature, title, step
from selenium.common.exceptions import WebDriverException, NoSuchWindowException, TimeoutException
from test_collections.suites_project_a.basetestcase import BaseTestCase


@feature("Demo用例")
class TestDemo(BaseTestCase):
    @classmethod
    def setup_class(cls):
        # 测试class前置步骤
        super().setup_class()

    @classmethod
    def teardown_class(cls):
        # 测试class后置步骤
        super().teardown_class()

    def setup_method(self):
        # 测试case前置步骤
        super().setup_method()

    def teardown_method(self):
        # 测试case后置步骤
        if self.user_actions.driver is not None:
            try:
                self.user_actions.driver.quit()
            except (WebDriverException, NoSuchWindowException, TimeoutException, AttributeError) as e:
                self.logger.error(e)
            finally:
                self.user_actions.driver = None

    @title("查询接口测试Demo")
    @pytest.mark.parametrize("data", BaseTestCase.ChecklistCaseData['CaseData']["s01"]['TestData']['TestData'])
    def test_id_s01_search_demo(self, data):
        """数据驱动Demo样例"""
        with step("第1步: 记录当前测试数据"):
            self.logger.info("第1步: 记录当前测试数据")
            self.logger.info("当前测试数据是:" + str(data))

        with step("第2步: 进行查询测试并断言"):
            self.logger.info("第2步: 进行查询测试并断言")
            self.user_actions.search_custom_business_obj(
                name=data["KeyWord"], expect=data["expect"], exist_data=data["exist_data"])
            self.logger.info(str(self.user_actions.api.headers))

    @title("业务场景Demo")
    def test_id_s02_action(self):
        """关键字驱动Demo样例"""
        with step("第1步: foo1"):
            self.logger.info("第1步: foo1")
            self.user_actions.business_api_action_1()

        with step("第2步: foo2"):
            self.logger.info("第2步: foo2")
            self.user_actions.page_action_1()

        with step("第3步: foo3"):
            self.logger.info("第3步: foo3")

        with step("第N步: fooN"):
            self.logger.info("第N步: fooN")
