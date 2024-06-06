# -*- coding: utf-8 -*-

"""
这是一个业务接口模块，封装了单个业务接口
1.接口封装命名规则：{Method}_{name}或者{Method}_{业务模块}_{name}
2.只封装接口，不涉及业务，故正常发出请求，返回Response即可,不做判断|期望|解析|异常处理

Attributes:

Functions:
    None

Classes:
    APIEndpoint:
        针对当前项目的接口类，封装了单个接口

"""

from hashlib import md5
from loguru import logger
from urllib.parse import urljoin
from lib.common.httpclient import HttpClient


class ApiEndpoint:
    @staticmethod
    def _foo1(*args, **kwargs):
        logger.info(kwargs)
        return md5(args[0] + args[1].encode('utf-8'))

    @staticmethod
    def __foo2(*args, **kwargs):
        pass

    def __init__(self):
        super().__init__()
        self.username = None
        self.password = None
        self.user_id = None
        self.api_host = None
        self.api = HttpClient()
        self.logger = logger

    # --------------- 登录和退出 --------------- #
    def post_login(self):
        """
        单个接口: 登录, post
        """
        if self.username is None and self.password is None and self.user_id is None:
            raise RuntimeError("登录前请传入账号和密码以及用户id(不能为None)")
        url = "/example/login"
        data = {
            "loginName": self.username,
            "password": self._foo1(self.password, self.username),
            "accountId": str(self.user_id)  # 用户注册时获得的唯一id
        }
        response = self.api.post(url=urljoin(self.api_host, url), json=data, verify=False)  # warnings=False
        return response

    def get_logout(self):
        """
        单个接口: 登出, get
        调用 account_id 进行登出
        """
        url = f"/example/logout/{self.user_id}"
        response = self.api.get(url=urljoin(self.api_host, url), verify=False)  # warnings=False
        return response

    # --------------- 业务接口 --------------- #
    def get_demo_api(self, **kwargs):
        """
        单个接口: get
        """
        url = "/example/get/api"
        params = kwargs
        response = self.api.get(url=urljoin(self.api_host, url), params=params, verify=False)  # warnings=False
        return response

    def post_demo_api(self, **kwargs):
        """
        单个接口: post
        """

        url = "/example/post/api"
        data = kwargs
        response = self.api.post(url=urljoin(self.api_host, url), json=data, verify=False)  # warnings=False
        return response
