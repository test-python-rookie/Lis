import data
import page
from base.base import Base
from page.page_login import PageLogin
from time import sleep
import time
import re

class PageRegister(Base):
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

    # 打开标本登记管理
    def page_open_register(self):
        # 标本分析前管理
        bbfxq = self.base_find_elements(page.bbfxq, page.bbfxq_num)
        # 鼠标悬停
        self.base_move_element(bbfxq)
        sleep(1)
        # 标本登记管理
        self.base_click(page.register)

    # 标本查询
    def page_register_query(self, sp_num):
        # 标本查询
        self.base_input(page.query_spnum, sp_num, page.query_spnum_num)
        sleep(1)
        self.base_click(page.query_register, page.query_register_num)
        sleep(2)
        # 获取标本号
        self.text = self.base_get_text(page.text)
        return self.text

    # 新增验单
    def page_register_create(self):
        # 标本查询
        self.base_click(page.query_register, page.query_register_num)
        sleep(1)
        # 点击新增验单按钮
        self.base_click(page.create_register, page.create_register_num)

    # 输入新增数据
    def page_register_data(self, zlkh, jyxm):
        # 诊疗卡号
        self.base_input(page.hospnum, zlkh, page.hospnum_num)
        self.base_active_input('Keys.ENTER')
        sleep(1)
        # 所属科室
        self.base_click(page.department1, page.department1_num)
        sleep(1)
        self.base_click(page.department2)
        sleep(1)
        # 主诊医生
        self.base_click(page.doctor1, page.doctor1_num)
        sleep(1)
        self.base_click(page.doctor2)
        sleep(1)
        # 检验项目
        for j in jyxm:
            self.base_input(page.inspection, j)
            self.base_active_input('Keys.ENTER')
            sleep(1)
        # 登记保存
        self.base_click(page.register_save)
        sleep(5)
        # 获取并关闭新打开的页面
        self.url = self.base_window_handles()
        # 提取url中的数字
        self.num = re.findall("\d+", self.url)
        print('登记成功生成标本号：', self.num[4], self.num[5])
        # 最新标本号
        self.sp_num = str(self.num[4])
        sleep(2)
        return self.sp_num

    # 截图
    def page_register_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)

    # 组装业务方法
    def page_register(self, zlkh, jyxm):
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        # sleep(1)
        self.page_open_register()
        sleep(2)
        self.page_register_create()
        sleep(2)
        self.sp_num = self.page_register_data(zlkh, jyxm)
        sleep(1)
        self.text = self.page_register_query(self.sp_num)
        return self.sp_num, self.text
