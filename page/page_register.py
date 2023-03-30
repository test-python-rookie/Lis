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
    def page_register_query(self):
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
        return self.sp_num

    # 新增验单
    def page_register_create(self):
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
        self.base_input(page.inspection, jyxm)
        self.base_active_input('Keys.ENTER')
        sleep(1)
        # 登记保存
        self.base_click(page.register_save)
        sleep(1)
        self.base_window_handles()
        sleep(2)
        # 获取标本最新数量文本
        self.text = self.base_get_text(page.text)
        # 提取数量
        self.num1 = re.findall("\d+", self.text)
        # 标本格式
        self.num2 = '{}000000'.format(time.strftime('%y%m%d'))
        # 最新标本号
        self.sp_num = int(self.num1[0]) + int(self.num2)
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
        self.sp_num_old = self.page_register_query()
        sleep(2)
        self.page_register_create()
        sleep(2)
        self.sp_num_new = self.page_register_data(zlkh, jyxm)
        return self.sp_num_old, self.sp_num_new
