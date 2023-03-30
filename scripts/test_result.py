import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_result import DataResult
from page.page_result import PageResult
from time import sleep


def get_data():
    return [(DataResult().input1, DataResult().input2, DataResult().input3, DataResult().input4, DataResult().input5)]

class TestResult(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取登录页面对象
        self.result = PageResult(GetDriver().get_driver())

    # 结束方法
    def tearDown(self):
        # 关闭浏览器
        GetDriver().quit_driver()

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_result(self, input1, input2, input3, input4, input5):
        # 调用测试方法
        self.type = self.result.page_result(input1, input2, input3, input4, input5)
        print(self.type)
        sleep(5)
        try:
            self.assertEqual(self.type[1], '已批准')
            self.result.page_result_assertionview(data.join_path, DataResult().successname)
            print('结果编辑审核成功！！！')
        except AssertionError as e:
            self.result.page_result_assertionview(data.join_path, DataResult().errorname)
            print('结果编辑审核失败！！！')
            raise AssertionError(e)

    if __name__ == '__main__':
        unittest.main()