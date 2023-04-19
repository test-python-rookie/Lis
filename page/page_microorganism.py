import re

import page
from base.base import Base
from time import sleep
import time

class PageMicroorganism(Base):
    # 登录
    # def __init__(self, driver):
    #     self.page_login = PageLogin(driver)
    #     self.page_login.page_login('admin01', '1234')
    #     self.driver = Base(self.page_login)
    # 输入用户名、密码
    def page_login_user(self):
        # 用户名
        self.base_input(page.username, "lisadmin", page.name_num)
        # 密码
        self.base_input(page.password, "123456", page.pwd_num)

    # 点击登录
    def page_login_btn(self):
        self.base_click(page.login)

    # 关闭结果审核页并刷新
    def page_refresh(self):
        # 标本查询
        self.base_click(page.spnum2, page.spnum2_num)
        sleep(1)
        # 获取普通标本号
        self.spp_num = self.base_get_text(page.result_spnum)
        self.sp_num = int(self.spp_num) + 1
        sleep(1)
        self.base_click(page.register_clock)
        sleep(1)
        self.base_refresh()
        return self.sp_num

    # 打开微生物结果审批管理
    def page_open_microorganism(self):
        # 标本分析中管理
        bbfxz = self.base_find_elements(page.bbfxz, page.bbfxz_num)
        # 鼠标悬停
        self.base_move_element(bbfxz)
        sleep(1)
        # 微生物结果审批管理
        self.base_click(page.microorganism)

    # 标本查询
    def page_microorganism_query(self, sp_num):
        # 输入标本号
        self.base_input(page.microorganism_spnum1, sp_num, page.microorganism_spnum1_num)
        # 标本查询
        self.base_click(page.microorganism_spnum2, page.microorganism_spnum2_num)
        # 获取标本当前状态
        self.type = self.base_get_text(page.microorganism_type)
        return self.type

    # 输入微生物结果编辑数据并审核
    def page_microorganism_data(self, microorganism_input):
        # 点击微生物结果编辑按钮
        self.base_click(page.microorganism_editing, page.microorganism_editing_num)
        sleep(1)
        # 输入微生物结果编辑数据
        self.base_input(page.microorganism_input, microorganism_input)
        sleep(1)
        # 微生物结果保存
        self.base_click(page.microorganism_save, page.microorganism_save_num)
        sleep(3)
        # 标本查询
        self.base_click(page.microorganism_spnum2, page.microorganism_spnum2_num)
        sleep(1)
        # 微生物结果审核
        self.base_click(page.microorganism_type)
        sleep(1)
        self.base_click(page.microorganism_audit1, page.microorganism_audit1_num)
        sleep(1)
        self.base_finds_click(page.microorganism_audit2, page.microorganism_audit2_num, page.microorganism_audit3, page.microorganism_audit3_num)
        sleep(3)
        # 标本查询
        self.base_click(page.microorganism_spnum2, page.microorganism_spnum2_num)
        sleep(1)
        # 获取标本审核后状态
        self.type = self.base_get_text(page.microorganism_type)
        sleep(3)
        return self.type

    #微生物结果批准
    def page_microorganism_approve(self):
        # 标本查询
        self.base_click(page.microorganism_spnum2, page.microorganism_spnum2_num)
        sleep(1)
        self.sp_num = self.base_get_text(page.microorganism_spnum)
        print('微生物结果批准使用标本号：', self.sp_num)
        # 获取微生物标本批准前状态
        self.type_old = self.base_get_text(page.microorganism_type)
        # 微生物结果批准
        self.base_click(page.microorganism_type)
        sleep(1)
        self.base_click(page.microorganism_approve, page.microorganism_approve_num)
        sleep(3)
        self.base_refresh()
        sleep(1)
        self.base_click(page.register_clock)
        sleep(1)
        self.base_refresh()
        sleep(1)
        self.page_open_microorganism()
        sleep(2)
        self.type_new = self.page_microorganism_query(str(self.sp_num))
        return self.type_old, self.type_new

    # 截图
    def page_microorganism_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)

    # 组装结果编辑审核业务方法
    def page_microorganism_audit(self, microorganism_input):
        # 获取标本号
        self.sp_num = self.page_refresh()
        print('微生物结果编辑使用标本号：', self.sp_num)
        # sleep(1)
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        sleep(3)
        self.page_open_microorganism()
        sleep(2)
        self.type_old = self.page_microorganism_query(str(self.sp_num))
        # self.type_old = self.page_microorganism_query('230418000027')
        sleep(2)
        self.type_new = self.page_microorganism_data(microorganism_input)
        return self.type_old, self.type_new

