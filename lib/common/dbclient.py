# -*- coding: utf-8 -*-

"""
这是一个MySQL数据库模块，封装了基本的数据库操作功能。

Attributes:

Functions:
    None

Classes:
    DBClient:
        一个简单的MySQL数据库操作类，提供连接、查询、插入、更新和删除等方法。
"""

import pymysql
from loguru import logger


class DBClient:
    """
    一个简单的MySQL数据库操作类，提供数据库连接及基本的CRUD操作。

    Attributes:
        host (str): 数据库地址。
        port (int): 数据库端口。
        user (str): 数据库用户名。
        password (str): 数据库密码。
        db (str): 数据库名。
        charset (str): 字符编码，默认为'utf8mb4'。
        connection (pymysql.Connection): 数据库连接实例。

    """

    def __init__(self, host, port, user, password, db, charset='utf8mb4'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.connection = None

    def connect(self):
        """
        建立到MySQL服务器的连接。
        """
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db,
                charset=self.charset
            )
            logger.info("Successfully connected to the database.")
        except Exception as e:
            logger.error(f"Error connecting to the database: {e}")

    def close(self):
        """
        关闭数据库连接。
        """
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed.")

    def query(self, sql, params=None):
        """
        执行SQL查询语句并返回结果。
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                logger.info(f"Query executed: {sql}, Params: {params}, Result: {result}")
                return result
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            return None

    def execute(self, sql, params=None):
        """
        执行SQL语句（如INSERT、UPDATE、DELETE）并返回受影响的行数。
        """
        try:
            with self.connection.cursor() as cursor:
                affected_rows = cursor.execute(sql, params)
                self.connection.commit()
                logger.info(f"SQL executed: {sql}, Params: {params}, Affected rows: {affected_rows}")
                return affected_rows
        except Exception as e:
            logger.error(f"Error executing SQL: {e}")
            self.connection.rollback()
            return None


# 使用示例：
if __name__ == "__main__":
    db_client = DBClient('localhost', 3306, 'username', 'password', 'database_name')
    db_client.connect()
    # 执行查询
    test_result = db_client.query("SELECT * FROM table_name")
    print(test_result)
    # 执行插入
    insert_result = db_client.execute("INSERT INTO table_name (column1, column2) VALUES (%s, %s)", ('value1', 'value2'))
    print(insert_result)
    db_client.close()
