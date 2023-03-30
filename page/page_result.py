import re

import page
from base.base import Base
from time import sleep
from page.page_register import PageRegister
import time

class PageResult(Base):
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

    # 关闭标本登记页并刷新
    def page_refresh(self):
        # 标本查询
        self.base_click(page.query_register, page.query_register_num)
        # 获取标本新增前最新数量文本
        self.text = self.base_get_text(page.text)
        # 提取数量
        self.num1 = re.findall("\d+", self.text)
        # 标本格式
        self.num2 = '{}000000'.format(time.strftime('%y%m%d'))
        # 标本新增前最新标本号
        self.sp_num = int(self.num1[0]) + int(self.num2)
        sleep(1)
        self.base_click(page.register_clock)
        sleep(1)
        self.base_refresh()
        return self.sp_num

    # 打开结果编辑审核管理
    def page_open_result(self):
        # 标本分析中管理
        bbfxz = self.base_find_elements(page.bbfxz, page.bbfxz_num)
        # 鼠标悬停
        self.base_move_element(bbfxz)
        sleep(1)
        # 结果编辑审核管理
        self.base_click(page.result)

    # 标本查询
    def page_result_query(self, sp_num):
        # 输入标本号
        self.base_input(page.spnum1, sp_num, page.spnum1_num)
        self.base_click(page.spnum2,page.spnum2_num)
        # 获取标本编辑前状态
        self.type = self.base_get_text(page.result_type)
        return self.type

    # 结果编辑
    def page_result_editing(self):
        # 点击结果编辑按钮
        self.base_click(page.result_editing, page.result_editing_num)

    # 输入结果编辑数据
    def page_result_data(self, input1, input2, input3, input4, input5):
        # 输入结果编辑数据
        self.base_input(page.input1, input1, page.input1_num)
        self.base_input(page.input2, input2, page.input2_num)
        self.base_input(page.input3, input3, page.input3_num)
        self.base_input(page.input4, input4, page.input4_num)
        self.base_input(page.input5, input5, page.input5_num)
        sleep(1)
        # 结果保存
        self.base_click(page.result_save, page.result_save_num)
        sleep(1)
        # 结果审核
        self.base_click(page.result_audit1, page.result_audit1_num)
        sleep(1)
        self.base_click(page.result_audit2, page.result_audit2_num)
        sleep(1)
        self.base_click(page.result_audit3, page.result_audit3_num)
        sleep(1)
        # 结果批准
        self.base_click(page.result_approve1, page.result_approve1_num)
        sleep(1)
        self.base_click(page.result_approve2, page.result_approve2_num)
        sleep(5)
        self.base_click(page.result_approve3, page.result_approve3_num)
        sleep(1)
        self.base_click(page.result_approve1, page.result_approve1_num)
        # 获取标本批准后状态
        self.type = self.base_get_text(page.result_type)
        return self.type

    # # 获取断言
    # def page_result_pass(self):
    #     return self.base_finds_text(page.request_text1, page.request_text1_num, page.request_text2, page.request_text2_num)

    # 截图
    def page_result_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)

    # 组装业务方法
    def page_result(self, input1, input2, input3, input4, input5):
        # 获取标本号
        self.sp_num = self.page_refresh()
        print('结果编辑使用标本号：', self.sp_num)
        # sleep(1)
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        sleep(3)
        self.page_open_result()
        sleep(2)
        self.type_old = self.page_result_query(str(self.sp_num))
        sleep(2)
        self.page_result_editing()
        sleep(2)
        self.type_new = self.page_result_data(input1, input2, input3, input4, input5)
        return self.type_old, self.type_new
