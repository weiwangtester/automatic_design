# -*- coding: utf-8 -*-

"""
这是一个页面元素模块，封装了用到的页面元素
1.接口封装命名规则：待定
2.只封装元素，不涉及业务

Attributes:

Functions:
    None

Classes:
    LocatorEndpoint:
        针对当前项目的接口类，封装了单个接口

"""

import time
from urllib.parse import urljoin, urlencode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from loguru import logger

Locators = {
    'Page1-Func1_ObjType_ObjName': "input.demo-input_inner[type='demo'][placeholder='Demo']",
}


def init_driver_login(func):
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, 'driver') or not self.driver:
            chrome_options = Options()
            # chrome_options.add_argument("--headless")  # 添加无头模式参数
            self.driver = webdriver.Chrome(options=chrome_options)  # 新建driver
            self.driver.implicitly_wait(15)  # 设置隐形等待超时为10秒
            self.driver.get(self.locator_host)  # 打开登录页面
            self.driver.maximize_window()  # 最大化页面
            time.sleep(10)
            pass  # 输入账号密码并点击登录
        else:
            pass
        self.driver.maximize_window()  # 最大化页面
        logger.info("Selenium Chrome driver inited.")
        # 调用原始方法
        return func(self, *args, **kwargs)

    return wrapper


class UiActions:
    """ui操作类"""

    def __init__(self):
        # super().__init__()
        self.locator_host = None
        self.headers = None
        self.driver = None
        self.actions = None
        self.logger = logger

    def _format_full_url(self, url, params=None):
        full_url = urljoin(self.locator_host, url)
        if params:
            query_string = urlencode(params)
            if '?' not in full_url:
                full_url += '?' + query_string
            else:
                # 如果已经存在查询字符串（例如URL重定向后），我们可能需要使用'&'来追加新的参数
                full_url += '&' + query_string
        return full_url

    @init_driver_login
    def foo4(self, *args, **kwargs):
        """
        UI动作1:
        """
        self.logger.info(args)
        url = "/example/#/demo/ui"
        params = kwargs
        self.driver.get(url=self._format_full_url(url, params))

        self.driver.find_element(By.CSS_SELECTOR, Locators["Page1-Func1_ObjType_ObjName"]).click()

        return None
