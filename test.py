import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 引用鼠标事件包
from selenium.webdriver.common.action_chains import ActionChains
# 引用键盘事件包
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://47.92.237.67/wamilis/#/login')
driver.maximize_window()
driver.implicitly_wait(10)
sleep(1)
# 登录
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[0].send_keys('lisadmin')
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[1].send_keys('123456')
sleep(1)
driver.find_element(By.CLASS_NAME, 'el-button').click()
sleep(1)
# 标本分析前管理
bbfxq = driver.find_elements(By.CLASS_NAME, 'el-submenu')[4]
# 鼠标悬浮
ActionChains(driver).move_to_element(bbfxq).perform()
sleep(1)
# 标本登记
# driver.find_element(By.XPATH, '/html/body/div[2]/ul/div').find_elements(By.CLASS_NAME, 'el-menu-item')[0].click()
driver.find_element(By.XPATH, '/html/body/div[2]/ul/div/div/li[1]').click()
sleep(2)
# 查询
driver.find_elements(By.CLASS_NAME, 'el-button--medium')[1].click()
sleep(2)
# 新增
driver.find_elements(By.CLASS_NAME, 'el-button--medium')[3].click()
sleep(2)
# 输入诊疗卡号
# hospnum = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[2]').find_elements(By.CLASS_NAME, 'el-input__inner')[1]
hospnum = driver.find_elements(By.CLASS_NAME, 'el-input__inner')[11]
hospnum.send_keys('2357')
sleep(2)
hospnum.send_keys(Keys.ENTER)
sleep(2)
# 输入所属科室
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[2]').find_elements(By.CLASS_NAME, 'el-input__inner')[3].click()
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[13].click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[4]').click()
sleep(2)
# 输入主诊医生
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[2]').find_elements(By.CLASS_NAME, 'el-input__inner')[14].click()
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[24].click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[4]').click()
sleep(2)
# 输入检验项目
inspection = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[4]/div/div[1]/div[1]/form/div[1]/div/div/div[1]/span/span/div/input')
inspection.send_keys('凝血4项')
sleep(1)
inspection.send_keys(Keys.ENTER)
sleep(2)
# 保存
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/button[4]').click()
sleep(1)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.close()
sleep(2)
driver.switch_to.window(all_handles[0])
sleep(1)
text = driver.find_element(By.CLASS_NAME, 'el-pagination__total').text
num1 = re.findall("\d+",text)
num2 = '{}000000'.format(time.strftime('%y%m%d'))
num3 = int(num1[0]) + int(num2)
print(num1, num2, num3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div/div[1]/div/span[2]/span').click()
sleep(1)
driver.refresh()
sleep(1)
# 标本分析中管理
bbfxz = driver.find_elements(By.CLASS_NAME, 'el-submenu')[5]
# 鼠标悬浮
ActionChains(driver).move_to_element(bbfxz).perform()
sleep(1)
# 结果编辑
driver.find_element(By.XPATH, '/html/body/div[2]/ul/div/div/li[1]').click()
sleep(2)
# 输入标本号
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[1].send_keys(num3)
sleep(1)
driver.find_elements(By.CLASS_NAME, 'el-button')[0].click()
sleep(1)
# 结果编辑按钮
driver.find_elements(By.CLASS_NAME, 'el-button')[5].click()
sleep(1)
# 输入信息
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[13].send_keys('12')
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[15].send_keys('3')
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[17].send_keys('20')
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[19].send_keys('12')
driver.find_elements(By.CLASS_NAME, 'el-input__inner')[21].send_keys('10')
sleep(2)
# 保存
driver.find_elements(By.CLASS_NAME, 'el-button')[6].click()
sleep(1)
# 审核
driver.find_elements(By.CLASS_NAME, 'el-button')[0].click()
sleep(1)
driver.find_elements(By.CLASS_NAME, 'el-button')[8].click()
sleep(1)
driver.find_elements(By.CLASS_NAME, 'el-button')[23].click()
sleep(1)
# 批准
driver.find_elements(By.CLASS_NAME, 'el-button')[0].click()
sleep(1)
driver.find_elements(By.CLASS_NAME, 'el-button')[10].click()
sleep(1)
driver.find_elements(By.CLASS_NAME, 'el-dialog__headerbtn')[3].click()
sleep(1)
driver.find_elements(By.CLASS_NAME, 'el-button')[0].click()
sleep(5)
# driver.find_elements(By.CLASS_NAME, 'el-select-dropdown__list')[7].find_elements(By.CLASS_NAME, 'el-select-dropdown__item')[4].click()
# sleep(2)
# # # 选择往来单位
# driver.find_elements(By.CLASS_NAME, 'el-dialog__body')[0].find_elements(By.CLASS_NAME, 'el-input__inner')[1].click()
# sleep(1)
# driver.find_elements(By.CLASS_NAME, 'el-select-dropdown__list')[7].find_elements(By.CLASS_NAME, 'el-select-dropdown__item')[1].click()
# # sleep(2)
# # 选择物品
# articles = driver.find_elements(By.CLASS_NAME, 'tbaleInputSkipToNextOne')[2]
# ActionChains(driver).double_click(articles).perform()
# # sleep(1)
# driver.switch_to.active_element.send_keys('10005')
# driver.switch_to.active_element.send_keys(Keys.ENTER)
# # driver.find_elements(By.CLASS_NAME, 'el-table__row')[33].click()
# # js3 = "document.getElementsByClassName('el-table__row')[33].click()"
# # driver.execute_script(js3)
# # sleep(1)
# # 输入数量
# articles = driver.find_elements(By.CLASS_NAME, 'tbaleInputSkipToNextOne')[3]
# ActionChains(driver).double_click(articles).perform()
# sleep(1)
# driver.switch_to.active_element.send_keys('5')
# sleep(1)
# # 修改出库单保存
# driver.find_elements(By.CLASS_NAME, 'el-button--medium')[7].click()
# save_time = time.strftime('%Y-%m-%d %H:%M')
# sleep(2)
# # 新增入库单确认
# # driver.find_elements(By.CLASS_NAME, 'el-button--medium')[4].click()
# # sleep(1)
# # driver.find_elements(By.CLASS_NAME, 'el-message-box')[1].find_elements(By.CLASS_NAME, 'el-button--primary')[0].click()
# # sleep(5)
# # 返回主表
# # driver.find_elements(By.CLASS_NAME, 'el-tabs__item')[0].click()
# # sleep(1)
# # 获取最新的录入时间
# text = driver.find_elements(By.CLASS_NAME, 'el-table__row')[0].find_elements(By.CLASS_NAME, 'el-tooltip')[8].text
# s_time = time.mktime(time.strptime(save_time, '%Y-%m-%d %H:%M'))
#
# if text == '':
#     print('失败')
# else:
#     t_time = time.mktime(time.strptime(text, '%Y-%m-%d %H:%M'))
#     if t_time >= s_time:
#         print('新增成功！')
#     else:
#         print('失败')





