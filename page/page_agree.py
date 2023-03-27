import page
from base.base import Base
from page.page_login import PageLogin
from time import sleep
import time

class PageAgree(Base):
    # 登录
    # def __init__(self, driver):
    #     self.page_login = PageLogin(driver)
    #     self.page_login.page_login('admin01', '1234')
    #     self.driver = Base(self.page_login)
    # 输入用户名、密码
    def page_login_user(self):
        # 用户名
        self.base_input(page.username, "qltest", page.name_num)
        # 密码
        self.base_input(page.password, "123456", page.pwd_num)

    # 点击登录
    def page_login_btn(self):
        self.base_click(page.login)

    # 打开入出库管理
    def page_open_inhouse_outhouse(self):
        self.base_click(page.inhouse_outhouse, page.inhouse_outhouse_num)

    # 点击修改审核申领单
    def page_agree_modify(self):
        # 打开申领管理页面
        self.base_click(page.agree, page.agree_num)
        sleep(1)
        # 点击修改申领单
        self.base_click(page.modify_agree, page.modify_agree_num)

    # 修改申领数据
    def page_agree_data(self, slsl):
        # 数量
        quantity = self.base_find_elements(page.agree_quantity)[page.agree_quantity_num]
        self.base_double_click(quantity)
        sleep(1)
        self.base_active_input(slsl)
        sleep(1)
        self.save_time = time.strftime('%Y-%m-%d %H:%M')
        # 申领单确认
        self.base_click(page.agree_confirm1, page.agree_confirm1_num)
        sleep(1)
        self.base_finds_click(page.agree_confirm2, page.agree_confirm2_num, page.agree_confirm3, page.agree_confirm3_num)
        # 申领单保存
        # self.base_click(page.agree_save, page.agree_save_num)
        # # 申领单取消
        # self.base_click(page.agree_cancel, page.agree_cancel_num)
        sleep(1)
        # 返回主表
        self.base_click(page.agree_master, page.agree_master_num)
        return self.save_time

    # 获取断言
    def page_agree_pass(self):
        return self.base_finds_text(page.agree_text1, page.agree_text1_num, page.agree_text2, page.agree_text2_num)

    # 截图
    def page_agree_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)

    # 组装业务方法
    def page_agree(self, slsl):
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        # sleep(3)
        # self.page_open_inhouse_outhouse()
        # sleep(1)
        self.page_agree_modify()
        sleep(2)
        self.save_time = self.page_agree_data(slsl)
        return self.save_time
