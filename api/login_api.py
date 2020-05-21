# 导包
import requests
# 创建登录api类
class TestLoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"

    def login(self, jsonData, headers):
        # IHRM项目可以直接发送登录请求
        # headers = {"Content-Type": "application/json"}
        # jsonData = {"mobile": "13800000002", "password": "123456"}
        # 发送登录请求
        response = requests.post(url=self.login_url, json=jsonData, headers=headers)
        return response