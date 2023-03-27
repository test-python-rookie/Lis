# 登录参数
class DataLogin:
    # 账号
    username = 'qltest'
    # 密码
    password = ('123456', '1234')
    # 断言比较
    expect = '首页'
    # 错误截图名称
    successname = '01_login_success'
    # 错误截图名称
    errorname = '01_login_error'

    # # 账号
    # def login_username(self):
    #     self.username = 'wmadmin'
    #     return self.username
    # # 密码
    # def login_password(self):
    #     self.password = '1234567'
    #     return self.password
    # # 断言比较
    # def login_expect(self):
    #     self.expect = 'http://47.92.237.67/materialsconsume/#/index'
    #     return self.expect
    # # 错误截图名称
    # def login_errorname(self):
    #     self.errorname = 'login'
    #     return self.errorname