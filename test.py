import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 引用鼠标事件包
from selenium.webdriver.common.action_chains import ActionChains
# 引用键盘事件包
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://47.92.237.67/materialsconsume/#/login')
driver.maximize_window()
sleep(2)
# 登录
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[0].send_keys('qltest')
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[1].send_keys('123456')
sleep(1)
driver.find_element(By.CLASS_NAME, 'el-button').click()
sleep(3)
# 入出库管理
driver.find_elements(By.CLASS_NAME, 'el-submenu__title')[1].click()
sleep(1)
# 出库管理
driver.find_elements(By.CLASS_NAME, 'el-menu-item')[4].click()
sleep(2)
# 新增出库单
driver.find_elements(By.CLASS_NAME, 'el-button--medium')[2].click()
sleep(2)
# 选择业务类型
driver.find_elements(By.CLASS_NAME, 'el-dialog__body')[0].find_elements(By.CLASS_NAME, 'el-input__inner')[0].click()
sleep(1)
driver.find_elements(By.CLASS_NAME, 'el-select-dropdown__list')[7].find_elements(By.CLASS_NAME, 'el-select-dropdown__item')[4].click()
sleep(2)
# # 选择往来单位
driver.find_elements(By.CLASS_NAME, 'el-dialog__body')[0].find_elements(By.CLASS_NAME, 'el-input__inner')[1].click()
sleep(1)
driver.find_elements(By.CLASS_NAME, 'el-select-dropdown__list')[7].find_elements(By.CLASS_NAME, 'el-select-dropdown__item')[1].click()
# sleep(2)
# 选择物品
articles = driver.find_elements(By.CLASS_NAME, 'tbaleInputSkipToNextOne')[2]
ActionChains(driver).double_click(articles).perform()
# sleep(1)
driver.switch_to.active_element.send_keys('10005')
driver.switch_to.active_element.send_keys(Keys.ENTER)
# driver.find_elements(By.CLASS_NAME, 'el-table__row')[33].click()
# js3 = "document.getElementsByClassName('el-table__row')[33].click()"
# driver.execute_script(js3)
# sleep(1)
# 输入数量
articles = driver.find_elements(By.CLASS_NAME, 'tbaleInputSkipToNextOne')[3]
ActionChains(driver).double_click(articles).perform()
sleep(1)
driver.switch_to.active_element.send_keys('5')
sleep(1)
# 修改出库单保存
driver.find_elements(By.CLASS_NAME, 'el-button--medium')[7].click()
save_time = time.strftime('%Y-%m-%d %H:%M')
sleep(2)
# 新增入库单确认
# driver.find_elements(By.CLASS_NAME, 'el-button--medium')[4].click()
# sleep(1)
# driver.find_elements(By.CLASS_NAME, 'el-message-box')[1].find_elements(By.CLASS_NAME, 'el-button--primary')[0].click()
# sleep(5)
# 返回主表
# driver.find_elements(By.CLASS_NAME, 'el-tabs__item')[0].click()
# sleep(1)
# 获取最新的录入时间
text = driver.find_elements(By.CLASS_NAME, 'el-table__row')[0].find_elements(By.CLASS_NAME, 'el-tooltip')[8].text
s_time = time.mktime(time.strptime(save_time, '%Y-%m-%d %H:%M'))

if text == '':
    print('失败')
else:
    t_time = time.mktime(time.strptime(text, '%Y-%m-%d %H:%M'))
    if t_time >= s_time:
        print('新增成功！')
    else:
        print('失败')





