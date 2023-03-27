import page
from base.base import Base
from time import sleep


class PageLogin(Base):
    # 输入用户名、密码
    def page_login_user(self, username, password):
        # 用户名
        self.base_input(page.username, username, page.name_num)
        # 密码
        self.base_input(page.password, password, page.pwd_num)

    # 点击登录
    def page_login_btn(self):
        sleep(1)
        self.base_click(page.login)

    # # 获取异常信息
    # def page_login_error(self):
    #     return self.base_get_text(page.error)
    #
    # # 获取通过信息
    # def page_login_pass(self):
    #     return self.base_get_text(page.succeed)

    # 获取断言信息
    def page_login_assert(self):
        return self.base_get_text(page.login_text, page.login_text_num)

    # 截图
    def page_login_assertionview(self,path,  assertionname):
        self.base_get_image(path, assertionname)

    # 组装业务方法
    def page_login(self, username, password):
        self.page_login_user(username, password)
        self.page_login_btn()