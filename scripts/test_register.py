import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_register import DataRegister
from page.page_register import PageRegister
from time import sleep
from selenium.webdriver.common.keys import Keys

def get_data():
    return [(DataRegister().zlkh, DataRegister().jyxm)]

class TestRegister(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取登录页面对象
        self.register = PageRegister(GetDriver().get_driver())

    # 结束方法
    # def tearDown(self):
    #     # 关闭浏览器
    #     GetDriver().quit_driver()

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_register(self, zlkh, jyxm):
        # 调用测试方法
        self.sp_num = self.register.page_register(zlkh, jyxm)
        print(self.sp_num)
        sleep(3)
        try:
            self.assertTrue(self.sp_num[0] < self.sp_num[1])
            self.register.page_register_assertionview(data.join_path, DataRegister().successname)
            print('标本登记成功！！！')
        except AssertionError as e:
            self.register.page_register_assertionview(data.join_path, DataRegister().errorname)
            print('标本登记失败！！！')
            raise AssertionError(e)

    if __name__ == '__main__':
        unittest.main()