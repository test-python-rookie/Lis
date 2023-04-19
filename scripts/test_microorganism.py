import time
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
import data
from data.data_microorganism import DataMicroorganism
from page.page_microorganism import PageMicroorganism
from time import sleep


def get_data():
    return [(DataMicroorganism().microorganism_input)]

class TestMicroorganism(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取登录页面对象
        cls.result = PageMicroorganism(GetDriver().get_driver())

    # 结束方法
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        GetDriver().quit_driver()

    # 新建结果编辑审核测试方法
    @parameterized.expand(get_data())
    def test_01_microorganism_audit(self, microorganism_input):
        # 调用测试方法
        self.type = self.result.page_microorganism_audit(microorganism_input)
        print('微生物标本编辑审核前状态：', self.type[0])
        print('微生物标本编辑审核后状态：', self.type[1])
        sleep(5)
        try:
            self.assertEqual(self.type[1], '已审核')
            self.result.page_microorganism_assertionview(data.join_path, '{}_audit'.format(DataMicroorganism().successname))
            print('微生物结果编辑审核成功！！！')
        except AssertionError as e:
            self.result.page_microorganism_assertionview(data.join_path, '{}_audit'.format(DataMicroorganism().errorname))
            print('微生物结果编辑审核失败！！！')
            raise AssertionError(e)

    # 新建结果批准测试方法
    def test_02_result_approve(self):
        # 调用测试方法
        self.type = self.result.page_microorganism_approve()
        print('微生物标本批准前状态：', self.type[0])
        print('微生物标本批准后状态：', self.type[1])
        sleep(5)
        try:
            self.assertEqual(self.type[1], '已批准')
            self.result.page_microorganism_assertionview(data.join_path, '{}_approve'.format(DataMicroorganism().successname))
            print('微生物结果批准成功！！！')
        except AssertionError as e:
            self.result.page_microorganism_assertionview(data.join_path, '{}_approve'.format(DataMicroorganism().errorname))
            print('微生物结果批准失败！！！')
            raise AssertionError(e)

    if __name__ == '__main__':
        unittest.main()