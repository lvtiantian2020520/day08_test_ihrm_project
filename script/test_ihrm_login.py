# 1.先用设计模式实现ihrm登录
# 2.根据设计模式的实现，封装ihrm登录接口
# 3.根据封装的接口，优化ihrm登录的代码

import unittest
import logging
import requests
from utils import assert_common

# 创建测试类，继承unittest.TestCase
class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        from api.login_api import TestLoginApi
        self.login_api = TestLoginApi()

    def tearDown(self):
        pass

    # 编写第一个案例，测试登录成功
    def test01_login_success(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登陆的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # # 断言登陆的结果
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, result.get("success"))
        # self.assertEqual(10000, result.get("code"))
        # self.assertIn("操作成功", result.get("message"))

        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

    def test02_mobile_is_not_exist(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13900000002", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登陆的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test03_password_is_error(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": "error"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登陆的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test04_mobile_is_empty(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "", "password": "error"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登陆的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test05_password_is_empty(self):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": ""}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登陆的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test06_mobile_has_special_char(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "138(0000002", "password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test07_more_params(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": "123456","more_params":"1"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, True, 10000, "操作成功", response, self)

    def test08_less_mobile(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"password": "123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test09_less_password(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile":"13800000002"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test10_none_params(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test11_error_params(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = {"mboile":"13800000002","password":"123456"}
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    def test12_None(self):
        # 定义请求头
        headers = {"Content-Type": "application/json"}
        jsonData = None
        # 发送登录请求
        response = self.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 断言
        assert_common(200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response, self)