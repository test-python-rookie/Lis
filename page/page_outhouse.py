import page
from base.base import Base
from page.page_login import PageLogin
from time import sleep
import time

class PageOuthouse(Base):
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

    # 点击修改出库单
    def page_outhouse_modify(self):
        # 打开出库管理页面
        self.base_click(page.outhouse, page.outhouse_num)
        sleep(3)
        # 点击修改出库单
        self.base_click(page.modify_outhouse, page.modify_outhouse_num)

    # 修改出库数据
    def page_outhouse_mdata(self):
        self.save_time = time.strftime('%Y-%m-%d %H:%M')
        # 出库单确认
        self.base_click(page.outhouse_confirm1, page.outhouse_confirm1_num)
        sleep(1)
        self.base_finds_click(page.outhouse_confirm2, page.outhouse_confirm2_num, page.outhouse_confirm3, page.outhouse_confirm3_num)
        # 申领单保存
        # self.base_click(page.outhouse_save, page.outhouse_save_num)
        # # 申领单取消
        # self.base_click(page.outhouse_cancel, page.outhouse_cancel_num)
        sleep(1)
        return self.save_time

    # 点击新增出库单
    def page_outhouse_create(self):
        # 打开出库管理页面
        self.base_click(page.outhouse, page.outhouse_num)
        sleep(3)
        # 点击新增出库单
        self.base_click(page.create_outhouse, page.create_outhouse_num)

    # 输入新增数据
    def page_outhouse_cdata(self, wpmc, cksl):
        # 业务类型
        self.base_finds_click(page.outhouse_business_type1, page.outhouse_business_type1_num, page.outhouse_business_type2, page.outhouse_business_type2_num)
        sleep(1)
        self.base_finds_click(page.outhouse_pull_down1, page.outhouse_pull_down1_num, page.outhouse_pull_down2, page.outhouse_pull_down2_num)
        sleep(1)
        # 往来单位
        self.base_finds_click(page.outhouse_ealing_unit1, page.outhouse_ealing_unit1_num, page.outhouse_ealing_unit2, page.outhouse_ealing_unit2_num)
        sleep(1)
        self.base_finds_click(page.outhouse_pull_down1, page.outhouse_pull_down1_num, page.outhouse_pull_down2, page.outhouse_pull_down2_num)
        # 物品
        articles = self.base_find_elements(page.outhouse_articles)[page.outhouse_articles_num]
        self.base_double_click(articles)
        sleep(1)
        self.base_active_input(wpmc)
        self.base_active_input('Keys.ENTER')
        # 数量
        quantity = self.base_find_elements(page.outhouse_quantity)[page.outhouse_quantity_num]
        self.base_double_click(quantity)
        sleep(1)
        self.base_active_input(cksl)
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
    def page_outhouse_pass(self):
        return self.base_finds_text(page.outhouse_text1, page.outhouse_text1_num, page.outhouse_text2, page.outhouse_text2_num)

    # 截图
    def page_outhouse_assertionview(self, path, assertionname):
        self.base_get_image(path, assertionname)

    # 组装修改业务方法
    def page_mouthouse(self):
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        # sleep(3)
        # self.page_open_inhouse_outhouse()
        # sleep(1)
        self.page_outhouse_modify()
        sleep(2)
        self.save_time = self.page_outhouse_mdata()
        return self.save_time

    # 组装新增业务方法
    def page_couthouse(self, wpmc, cksl):
        # self.page_login_user()
        # sleep(1)
        # self.page_login_btn()
        # sleep(3)
        # self.page_open_inhouse_outhouse()
        # sleep(1)
        self.page_outhouse_create()
        sleep(2)
        self.save_time = self.page_outhouse_cdata(wpmc, cksl)
        return self.save_time
