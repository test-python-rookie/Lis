import time
from selenium.webdriver.support.wait import WebDriverWait
# 引用鼠标事件包
from selenium.webdriver.common.action_chains import ActionChains
# # 引用键盘事件包
from selenium.webdriver import Keys

class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法（提供：点击、输入、获取文本）使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_find_elements(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    def base_finds_elements(self, loc1, num1, loc2, num2, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc1)[num1].find_elements(*loc2)[num2])

    # 获取当前焦点元素
    def base_active_element(self):
        return self.driver.switch_to.active_element

    # 点击方法
    def base_click(self, loc, num=None):
        if num is None:
            self.base_find_element(loc).click()
        else:
            self.base_find_elements(loc)[num].click()

    # 双重元素定位点击方法
    def base_finds_click(self, loc1, num1, loc2, num2):
        self.base_finds_elements(loc1, num1, loc2, num2).click()

    # 鼠标双击方法
    def base_double_click(self, double):
        ActionChains(self.driver).double_click(double).perform()

    # 输入方法
    def base_input(self, loc, value, num=None):
        if num is None:
            el = self.base_find_element(loc)
        else:
            el = self.base_find_elements(loc)[num]
        # 清空
        el.clear()
        el.send_keys(*value)

    # 获取文本方法
    def base_get_text(self, loc, num=None):
        if num is None:
            return self.base_find_element(loc).text
        else:
            return self.base_find_elements(loc)[num].text

    # 双重元素定位获取文本方法
    def base_finds_text(self, loc1, num1, loc2, num2):
        return self.base_finds_elements(loc1, num1, loc2, num2).text

    # 当前焦点输入
    def base_active_input(self, value):
        if value == 'Keys.ENTER':
            el = self.base_active_element()
            el.send_keys(Keys.ENTER)
        else:
            el = self.base_active_element()
            el.clear()
            el.send_keys(*value)

    # 获取当前页面url
    def base_get_url(self):
        return self.driver.current_url

    # 截图方法
    def base_get_image(self, path, assertionname):
        # print(path)
        self.driver.get_screenshot_as_file('{}/{}_{}.png'.format(path, assertionname, time.strftime('%Y%m%d%H%M%S')))