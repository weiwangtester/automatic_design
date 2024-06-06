# -*- coding: utf-8 -*-

"""
这是一个业务操作模块，封装了“多个接口组装而成”的多种业务操作
1.接口封装命名规则：{Method}_{name}或者{Method}_{业务模块}_{name}
2.只封装接口，不涉及业务，故正常发出请求，返回Response即可

Attributes:

Functions:
    None

Classes:
    UserActions:
        继承自单个接口模块，调用父类的方法，组装出不同业务操作，供测试用例调用
        传入测试网址、测试用户名和测试密码，自动登录并获取token

"""

from test_collections.suites_project_a.action_collection.api_endpoints import ApiEndpoint


class ApiActions(ApiEndpoint):
    def __init__(self):
        super().__init__()
        self.headers = None
        self.cookies = None

    def _action_login(self, expect=True):
        """
        业务动作: 登录
        通过调用登录接口实现
        """
        response = self.post_login()
        if expect:
            assert response.json()["code"] == "0"
            pass  # 处理header和cookies
        else:
            assert response.json()["code"] != "0"

    def business_api_action_1(self, expect=True
                              ):
        """
        业务动作: action_1
        """
        response1 = self.get_demo_api()
        response2 = self.post_demo_api()
        if expect:
            assert response1.json()["code"] == "0" and response2.json()["code"] == "0"
            return response1.json(), response2.json()
        else:
            assert response1.json()["code"] != "0" or response2.json()["code"] == "0"
            return None, None
