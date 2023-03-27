import page
from base.base import Base
from page.page_login import PageLogin
from time import sleep
import time

class PageInhouse(Base):
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

    # 点击新增入库单
    def page_inhouse_create(self):
        # 打开入库管理页面
        self.base_click(page.inhouse, page.inhouse_num)
        # 点击新增入库单
        self.base_click(page.create_inhouse, page.create_inhouse_num)

    # 输入新增数据
    def page_inhouse_data(self, wpmc, rksl):
        # 业务类型
        self.base_click(page.business_type, page.business_type_num)
        sleep(1)
        self.base_finds_click(page.pull_down1, page.pull_down1_num, page.pull_down2, page.pull_down2_num)
        sleep(1)
        # 往来单位
        self.base_click(page.ealing_unit, page.ealing_unit_num)
        sleep(1)
        self.base_finds_click(page.pull_down1, page.pull_down1_num, page.pull_down2, page.pull_down2_num)
        # 物品
        articles = self.base_find_elements(page.inhouse_articles)[page.inhouse_articles_num]
        self.base_double_click(articles)
        sleep(1)
        self.base_active_input(wpmc)
        self.base_active_input('Keys.ENTER')
        # 数量
        quantity = self.base_find_elements(page.inhouse_quantity)[page.inhouse_quantity_num]
        self.base_double_click(quantity)
        sleep(1)
        self.base_active_input(rksl)
        sleep(1)
        # 有效期
        today = self.base_find_elements(page.inhouse_today)[page.inhouse_today_num]
        self.base_double_click(today)
        self.base_active_input(time.strftime('%Y-%m-%d'))
        sleep(1)
        self.save_time = time.strftime('%Y-%m-%d %H:%M')
        # 入库单确认
        self.base_click(page.inhouse_confirm1, page.inhouse_confirm1_num)
        sleep(1)
        self.base_finds_click(page.inhouse_confirm2, page.inhouse_confirm2_num, page.inhouse_confirm3, page.inhouse_confirm3_num)
        # 入库单保存
        # self.base_click(page.inhouse_save, page.inhouse_save_num)
        # 入库单取消
        # self.base_click(page.inhouse_cancel, page.inhouse_cancel_num)
        return self.save_time

    # 获取断言
    def page_inhouse_pass(self):
        return self.base_finds_text(page.inhouse_text1, page.inhouse_text1_num, page.inhouse_text2, page.inhouse_text2_num)

    # 截图
    def page_inhouse_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)

    # 组装业务方法
    def page_inhouse(self, wpmc, rksl):
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        sleep(3)
        self.page_open_inhouse_outhouse()
        sleep(1)
        self.page_inhouse_create()
        sleep(1)
        self.save_time = self.page_inhouse_data(wpmc, rksl)
        return self.save_time
