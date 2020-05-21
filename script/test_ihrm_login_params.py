
import unittest
import logging
import requests
from parameterized import parameterized

import app
from utils import assert_common, read_login_data


# 创建测试类，继承unittest.TestCase
class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        from api.login_api import TestLoginApi
        self.login_api = TestLoginApi()

    def tearDown(self):
        pass

    filename = app.BASE_DIR + "/data/login_data.json"
    @parameterized.expand(read_login_data(filename))
    # 编写第一个案例，测试登录成功
    def test01_login(abc, case_name, jsonData, http_code, success, code, message):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = jsonData
        # 发送登录请求
        response = abc.login_api.login(jsonData, headers)
        # 打印登陆的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))

        # 断言
        assert_common(http_code, success, code, message, response, abc)