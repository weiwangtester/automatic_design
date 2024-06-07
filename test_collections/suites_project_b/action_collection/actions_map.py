# -*- coding: utf-8 -*-

"""
user_action的foo映射
用字典的key或者数据表的主键保证id唯一
"""

from test_collections.suites_project_b.action_collection.user_actions import UserActions

ActionsMap = {
    "1": UserActions.initialize_data,
    "3": UserActions.initialize_env,
    "10": UserActions.login,
    "15": UserActions.search_user_info,
    "19": UserActions.foo4,
}
