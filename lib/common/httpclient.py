# -*- coding: utf-8 -*-

"""
这是一个http|https模块，封装了http|https协议的基础功能

Attributes:

Functions:
    None

Classes:
    HttpClient:
        一个简单的http|https协议类，可以进行简单的post和get

"""

import requests
from loguru import logger


class HttpClient:
    """
    一个简单的Http|Https协议类，提供get、post、put和delete方法封装。

    Attributes:
        headers (dict): 请求头，默认为空字典。
        session (requests.Session): 请求会话实例，用于保持会话状态。

    """

    def __init__(self):
        self.headers = {}
        self.session = requests.session()  # 创建请求会话

    def get(self, url, **kwargs):
        logger.info(f"Request: Method: Get, URL: {url}, **kwargs: {kwargs}")  # 记录请求信息
        response = self.session.get(url=url, headers=self.headers, **kwargs)  # 执行GET请求
        try:
            logger.info(f"Response: {response.json()}")
        except:
            pass  # 忽略响应解析异常
        return response  # 返回响应对象

    def post(self, url, data=None, json=None, **kwargs):
        logger.info(f"Request: Method: Post, URL: {url}, Data: {data}, Json: {json}")  # 记录请求信息
        response = self.session.post(url=url, headers=self.headers, data=data, json=json, **kwargs)  # 执行POST请求
        try:
            logger.info(f"Response: {response.json()}")
        except:
            pass  # 忽略响应解析异常
        return response  # 返回响应对象

    def put(self, url, data=None, **kwargs):
        logger.info(f"Request: Method: Put, URL: {url}, Data: {data}")  # 记录请求信息
        response = self.session.put(url=url, headers=self.headers, data=data, **kwargs)  # 执行PUT请求
        try:
            logger.info(f"Response: {response.json()}")
        except:
            pass  # 忽略响应解析异常
        return response  # 返回响应对象

    def delete(self, url, **kwargs):
        logger.info(f"Request: Method: Delete, URL: {url}")  # 记录请求信息
        response = self.session.delete(url=url, headers=self.headers, **kwargs)  # 执行DELETE请求
        try:
            logger.info(f"Response: {response.json()}")
        except:
            pass  # 忽略响应解析异常
        return response  # 返回响应对象
