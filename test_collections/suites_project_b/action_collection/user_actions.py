# -*- coding: utf-8 -*-

"""
这是一个业务操作模块，封装了多种业务操作

Attributes:

Functions:
    None

"""

from test_collections.suites_project_b.action_collection.api_actions import ApiActions
from test_collections.suites_project_b.action_collection.locator_actions import UiActions


def _format_host(host):
    """
    初始化在构造方法中传入的host
    Parameters:
        host (str): 网址host. example: a.b.c.d 或 1.2.3.4
    Returns:
        host (str): 处理完毕的host, 前方加上了 https://, 后方去掉了/
    """
    if host.startswith("http://"):
        host = host.replace("http://", "https://")
    if not host.startswith("https://"):
        host = "https://" + host
    while True:
        if host.endswith("/"):
            host = host[:-1]
        else:
            break
    return host


class UserActions(ApiActions, UiActions):
    """集成接口动作类和UI动作类"""

    def __init__(self, api_host, locator_host, username, password, user_id):
        super().__init__()
        self.username = username
        self.password = password
        self.user_id = user_id
        self.api_host = api_host
        self.locator_host = locator_host

        self.cookies = None

        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        self.api.headers = self.headers
        self._action_login()  # 登录, 获取 self.cookies

    def initialize_data(self, *args, **kwargs):
        """
        业务动作: 初始化测试数据
        action_id: 1
        """
        self.logger.info(args)
        self.logger.info(kwargs)
        pass  # 初始化数据步骤

    def initialize_env(self, *args, **kwargs):
        """
        业务动作: 初始化测试环境
        action_id: 3
        """
        self.logger.info(args)
        self.logger.info(kwargs)
        pass  # 初始化环境步骤
