import os
import glob
import data
import unittest


if __name__ == '__main__':
    for file_name in glob.glob('{}/*'.format(data.join_path)):
        os.remove(file_name)
        # print(file_name)
    case_login = unittest.defaultTestLoader.discover('./scripts', pattern="test_login.py")
    case_inhouse = unittest.defaultTestLoader.discover('./scripts', pattern="test_inhouse.py")
    case_request = unittest.defaultTestLoader.discover('./scripts', pattern="test_request.py")
    case_agree = unittest.defaultTestLoader.discover('./scripts', pattern="test_agree.py")
    case_outhouse = unittest.defaultTestLoader.discover('./scripts', pattern="test_outhouse.py")
    # 创建套件
    suit = unittest.TestSuite()
    # 添加套件用例
    suit.addTest(case_login)
    suit.addTest(case_inhouse)
    suit.addTest(case_request)
    suit.addTest(case_agree)
    suit.addTest(case_outhouse)
    run = unittest.TextTestRunner()
    run.run(suit)



