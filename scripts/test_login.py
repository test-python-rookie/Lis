import unittest
from parameterized import parameterized
from page.page_login import PageLogin
from time import sleep
from base.get_driver import GetDriver
import data
from data.data_login import DataLogin

def get_data():
#    return [('wmadmin', '123456', url), ('wmadmin', '1234', url)]
    return [(DataLogin().username, DataLogin().password[0], DataLogin().expect)]

class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取登录页面对象
        self.login = PageLogin(GetDriver().get_driver())

    # 结束方法
    # def tearDown(self):
    #     # 关闭浏览器
    #     GetDriver().quit_driver()

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, password, expect):
        # 调用测试登录方法
        self.login.page_login(username, password)
        sleep(2)
        # 获取断言
        msg = self.login.page_login_assert()
        try:
            self.assertEqual(msg, expect)
            self.login.page_login_assertionview(data.join_path, DataLogin().successname)
            print('登录成功！！！')
            # print('url地址为：', DataLogin().successname)
        except AssertionError:
            self.login.page_login_assertionview(data.join_path, DataLogin().errorname)
            print('登录失败！！！')
            # print('url地址为：', msg)

    if __name__ == '__main__':
        unittest.main()