# 导包
import unittest

import HTMLTestRunner_PY3

import app
from script.test_ihrm_employee_params import TestIHRMEmployee3
from script.test_ihrm_login_params import TestIHRMLogin


# 创建测试套件
suite = unittest.TestSuite()

# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmployee3))

# 定义测试报告的名称
report_name = app.BASE_DIR + "/report/ihrm.html"

with open(report_name, 'wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=2,title="IHRM接口测试报告",
                                               description="人力资源管理系统测试报告")
    runner.run(suite)
