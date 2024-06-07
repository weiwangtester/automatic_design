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

from test_collections.suites_project_b.action_collection.api_endpoints import ApiEndpoint


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

    def login(self, username, password, user_id, expect=True):
        """
        业务动作: 指定用户登录
        action_id: 10
        """
        self.get_logout()  # 先退出默认登录的账户
        self.username = username
        self.password = password
        self.user_id = user_id
        self._action_login(expect)

    def search_user_info(self, username, expect=True):
        """
        业务动作: 搜索用户信息
        action_id: 10
        """
        response = self.get_user_info(username=username)
        if expect:
            assert response.json()["code"] == "0"
        else:
            assert response.json()["code"] != "0"
