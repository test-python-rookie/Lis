import HTMLTestRunner
import os
import glob
import time
import data
import unittest


if __name__ == '__main__':
    for file_name in glob.glob('{}/*'.format(data.join_path)):
        os.remove(file_name)
    case_login = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_login.py")
    case_register = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_register.py")
    case_result = unittest.defaultTestLoader.discover(data.scripts_path, pattern="test_result.py")
    # # 创建套件
    # suit = unittest.TestSuite()
    # # 添加套件用例
    # suit.addTest(case_login)
    # suit.addTest(case_register)
    # suit.addTest(case_result)
    # run = unittest.TextTestRunner()
    # run.run(suit)
    # 生成测试报告
    report_file_path = data.report_path + '/test_report_{}.html'.format(time.strftime('%Y%m%d%H%M%S'))
    with open(report_file_path,'wb') as f:
        print(report_file_path)
        # 创建套件
        suit = unittest.TestSuite()
        # 添加套件用例
        suit.addTest(case_login)
        suit.addTest(case_register)
        suit.addTest(case_result)
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='',description='',verbosity=2)
        runner.run(suit)



