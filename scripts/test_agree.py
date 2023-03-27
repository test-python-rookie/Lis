import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_agree import DataAgree
from page.page_agree import PageAgree
from time import sleep
from selenium.webdriver.common.keys import Keys

def get_data():
    return [(DataAgree().slsl)]

class TestAgree(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取登录页面对象
        self.agree = PageAgree(GetDriver().get_driver())

    # 结束方法
    # def tearDown(self):
    #     # 关闭浏览器
    #     GetDriver().quit_driver()

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_agree(self, slsl):
        # 调用测试方法
        save_time = self.agree.page_agree(slsl)
        sleep(3)
        # 获取断言
        text_time = self.agree.page_agree_pass()
        s_time = time.mktime(time.strptime(save_time, '%Y-%m-%d %H:%M'))
        try:
            self.assertNotEqual(text_time, '')
            try:
                t_time = time.mktime(time.strptime(text_time, '%Y-%m-%d %H:%M'))
                self.assertTrue(t_time >= s_time)
                self.agree.page_agree_assertionview(data.join_path, DataAgree().successname)
                print('审核申领单成功！！！')
            except AssertionError:
                self.agree.page_agree_assertionview(data.join_path, DataAgree().errorname)
                print('审核申领单失败！！！')
        except AssertionError:
            self.agree.page_agree_assertionview(data.join_path, DataAgree().errorname)
            print('审核申领单失败！！！')

    if __name__ == '__main__':
        unittest.main()