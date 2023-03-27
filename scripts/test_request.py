import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_request import DataRequest
from page.page_request import PageRequest
from time import sleep
from selenium.webdriver.common.keys import Keys


def get_data():
    return [(DataRequest().wpmc, DataRequest().qlsl)]

class TestRequest(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取登录页面对象
        self.request = PageRequest(GetDriver().get_driver())

    # 结束方法
    # def tearDown(self):
    #     # 关闭浏览器
    #     GetDriver().quit_driver()

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_request(self, wpmc, qlsl):
        # 调用测试方法
        save_time = self.request.page_request(wpmc, qlsl)
        sleep(3)
        # 获取断言
        text_time = self.request.page_request_pass()
        s_time = time.mktime(time.strptime(save_time, '%Y-%m-%d %H:%M'))
        t_time = time.mktime(time.strptime(text_time, '%Y-%m-%d %H:%M'))
        try:
            self.assertTrue(t_time >= s_time)
            self.request.page_request_assertionview(data.join_path, DataRequest().successname)
            print('新增请领单成功！！！')
        except AssertionError:
            self.request.page_request_assertionview(data.join_path, DataRequest().errorname)
            print('新增请领单失败！！！')

    if __name__ == '__main__':
        unittest.main()