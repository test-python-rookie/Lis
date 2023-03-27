import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_outhouse import DataOuthouse
from page.page_outhouse import PageOuthouse
from time import sleep
from selenium.webdriver.common.keys import Keys


def get_data():
    return [(DataOuthouse().wpmc, DataOuthouse().cksl)]

class TestOuthouse(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取登录页面对象
        cls.outhouse = PageOuthouse(GetDriver().get_driver())

    # 结束方法
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        GetDriver().quit_driver()

    # 新建修改测试方法
    # @parameterized.expand(get_data())
    def test_01_mouthouse(self):
        # 调用测试方法
        self.save_time = self.outhouse.page_mouthouse()
        sleep(3)
        # 获取断言
        self.text_time = self.outhouse.page_outhouse_pass()
        self.s_time = time.mktime(time.strptime(self.save_time, '%Y-%m-%d %H:%M'))
        try:
            self.assertNotEqual(self.text_time, '')
            try:
                self.t_time = time.mktime(time.strptime(self.text_time, '%Y-%m-%d %H:%M'))
                self.assertTrue(self.t_time >= self.s_time)
                self.outhouse.page_outhouse_assertionview(data.join_path, '{}_modify'.format(DataOuthouse().successname))
                print('审核修改出库单成功！！！')
            except AssertionError:
                self.outhouse.page_outhouse_assertionview(data.join_path, '{}_modify'.format(DataOuthouse().errorname))
                print('审核修改出库单失败！！！')
        except AssertionError:
            self.outhouse.page_outhouse_assertionview(data.join_path, '{}_modify'.format(DataOuthouse().errorname))
            print('审核申领单失败！！！')

    # 新建新增测试方法
    @parameterized.expand(get_data())
    def test_02_couthouse(self, wpmc, cksl):
        # 调用测试方法
        self.save_time = self.outhouse.page_couthouse(wpmc, cksl)
        sleep(3)
        # 获取断言
        self.text_time = self.outhouse.page_outhouse_pass()
        self.s_time = time.mktime(time.strptime(self.save_time, '%Y-%m-%d %H:%M'))
        try:
            self.assertNotEqual(self.text_time, '')
            try:
                self.t_time = time.mktime(time.strptime(self.text_time, '%Y-%m-%d %H:%M'))
                self.assertTrue(self.t_time >= self.s_time)
                self.outhouse.page_outhouse_assertionview(data.join_path, '{}_create'.format(DataOuthouse().successname))
                print('审核新增出库单成功！！！')
            except AssertionError:
                self.outhouse.page_outhouse_assertionview(data.join_path, '{}_create'.format(DataOuthouse().errorname))
                print('审核新增出库单失败！！！')
        except AssertionError:
            self.outhouse.page_outhouse_assertionview(data.join_path, '{}_create'.format(DataOuthouse().errorname))
            print('审核新增出库单失败！！！')

    if __name__ == '__main__':
        unittest.main()