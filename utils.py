
import json

# 通用断言函数
def assert_common(httpcode, success, code, message, response, self):
    self.assertEqual(httpcode, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

# 读取登录数据的函数
def read_login_data(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = list()
        for login_data in jsonData:
            result_list.append(tuple(login_data.values()))
        print("提取的结果为: ", result_list)
        return result_list

def read_emp_data(filename, name):
    with open(filename, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        emp_data = jsonData.get(name)
        result_list = list()
        result_list.append(tuple(emp_data.values()))
    print(result_list)
    return result_list

if __name__ == '__main__':
    import app
    # filename = app.BASE_DIR + "/data/login_data.json"
    # print("filename的路径为: ", filename)
    # read_login_data(filename)

    filename = app.BASE_DIR + "/data/emp_data.json"
    read_emp_data(filename,"add_emp")
    read_emp_data(filename, "query_emp")
    read_emp_data(filename, "modify_emp")
    read_emp_data(filename, "delete_emp")
