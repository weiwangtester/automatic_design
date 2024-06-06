# -*- coding: utf-8 -*-

"""
这是一个FTP客户端模块，封装了FTP服务器的基本操作功能。

Attributes:

Functions:
    None

Classes:
    FtpClient:
        一个简单的FTP客户端类，提供连接、上传、下载、列出目录及关闭连接等方法。
"""

import ftplib
from loguru import logger


class FtpClient:
    """
    一个简单的FTP客户端类，提供FTP服务器的基本操作。

    """

    def __init__(self, host, port=21, user='', password=''):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.ftp = None

    def connect(self):
        """
        连接到FTP服务器。
        """
        try:
            self.ftp = ftplib.FTP()
            self.ftp.connect(host=self.host, port=self.port)
            self.ftp.login(user=self.user, passwd=self.password)
            logger.info("Successfully connected to the FTP server.")
        except ftplib.all_errors as e:
            logger.error(f"Error connecting to the FTP server: {e}")

    def disconnect(self):
        """
        断开与FTP服务器的连接。
        """
        if self.ftp:
            self.ftp.quit()
            logger.info("Disconnected from the FTP server.")

    def upload(self, local_file_path, remote_directory):
        """
        将本地文件上传到FTP服务器指定目录。
        """
        try:
            with open(local_file_path, 'rb') as file:
                remote_file_path = remote_directory + '/' + local_file_path.split('/')[-1]
                self.ftp.storbinary(f'STOR {remote_file_path}', file)
                logger.info(f"Uploaded file {local_file_path} to {remote_file_path}")
        except ftplib.all_errors as e:
            logger.error(f"Error uploading file: {e}")

    def download(self, remote_file_path, local_directory):
        """
        从FTP服务器下载文件到本地指定目录。
        """
        try:
            with open(local_directory + '/' + remote_file_path.split('/')[-1], 'wb') as file:
                self.ftp.retrbinary(f'RETR {remote_file_path}', file.write)
                logger.info(f"Downloaded file {remote_file_path} to {local_directory}")
        except ftplib.all_errors as e:
            logger.error(f"Error downloading file: {e}")

    def list_directory(self, directory='.', detail=False):
        """
        列出FTP服务器指定目录的内容。
        """
        try:
            if detail:
                lines = []
                self.ftp.retrlines(f'LIST {directory}', lines.append)
                files = [line.split(None, 8)[8] for line in lines if line.startswith('-')]
                dirs = [line.split(None, 8)[8] for line in lines if line.startswith('d')]
                return {'files': files, 'directories': dirs}
            else:
                return self.ftp.nlst(directory)
        except ftplib.all_errors as e:
            logger.error(f"Error listing directory: {e}")
            return None


# 使用示例：
if __name__ == "__main__":
    ftp_client = FtpClient('ftp.example.com', user='username', password='password')
    ftp_client.connect()
    # 上传文件
    ftp_client.upload('/path/to/local/file.txt', '/remote/directory/')
    # 下载文件
    ftp_client.download('/remote/file.txt', '/local/directory/')
    # 列出目录内容
    contents = ftp_client.list_directory('/')
    print(contents)
    ftp_client.disconnect()
