# AutoTest自动化测试框架使用指南

## 简介

当前框架使用 pytest 三方库实现自动化测试

基于 requests 实现接口测试、基于 selenium 实现 UI 测试

可以关键字驱动，也可以数据驱动

## 安装

- [ ] 安装 python 3.12 版本
- [ ] 使用 pip 安装三方库
- [ ] 本地安装 allure
- [ ] [下载符合本地 Chrome 版本的 Driver](https://googlechromelabs.github.io/chrome-for-testing/) Driver
  文件放到项目根目录即可，不用上传到 git

```
pip install -r requirements.txt
```

## 编写用例

- [ ] 在 test_collections 下的项目中封装 业务接口
- [ ] 在 test_collections 下的项目中用 业务接口 封装 业务场景
- [ ] 在 test_collections 下的项目中用 业务场景 封装 测试用例
- [ ] 在 test_collections 下的项目中的 conftest 编写需要的 fixture
- [ ] 在 test_collections 下的项目中的 用例基类中 编写 公共步骤

## 编写工具类

- [ ] 在 lib 下编写各种 公共的 和业务无关的 工具类和插件

## 日志对象

日志对象全局唯一，在根目录的 conftest.py 中初始化并配置完毕

* 在用例中，直接通过 self.logger 使用即可
* 在其他位置 from logure import logger 导入后，即可使用

## 测试报告

测试报告位于 report 目录下

* runcase.log: 使用 log 记录下的 log
* json_report: 原始的 allure 测试报告 json 数据
* 其余文件: 生成的 html 格式的 allure 测试报告


