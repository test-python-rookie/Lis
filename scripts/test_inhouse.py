import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_inhouse import DataInhouse
from page.page_inhouse import PageInhouse
from time import sleep
from selenium.webdriver.common.keys import Keys

def get_data():
    return [(DataInhouse().wpmc, DataInhouse().rksl)]

class TestInhouse(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取登录页面对象
        self.inhouse = PageInhouse(GetDriver().get_driver())

    # 结束方法
    # def tearDown(self):
    #     # 关闭浏览器
    #     GetDriver().quit_driver()

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_inhouse(self, wpmc, rksl):
        # 调用测试方法
        save_time = self.inhouse.page_inhouse(wpmc, rksl)
        sleep(3)
        # 获取断言
        text_time = self.inhouse.page_inhouse_pass()
        s_time = time.mktime(time.strptime(save_time, '%Y-%m-%d %H:%M'))
        t_time = time.mktime(time.strptime(text_time, '%Y-%m-%d %H:%M'))
        try:
            self.assertTrue(t_time >= s_time)
            self.inhouse.page_inhouse_assertionview(data.join_path, DataInhouse().successname)
            print('新增入库单成功！！！')
        except AssertionError:
            self.inhouse.page_inhouse_assertionview(data.join_path, DataInhouse().errorname)
            print('新增入库单失败！！！')

    if __name__ == '__main__':
        unittest.main()