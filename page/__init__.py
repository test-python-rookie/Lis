from selenium.webdriver.common.by import By

# url
url = r'http://39.98.72.93/wamilis/#/login'

# 用户名
username = By.CLASS_NAME, 'el-input__inner'
name_num = 0

# 密码
password = By.CLASS_NAME, 'el-input__inner'
pwd_num = 1

# 登录按钮
login = By.CLASS_NAME, 'el-button'

# 首页
login_text = By.CLASS_NAME, 'tags-view-item'

# 标本分析前管理
bbfxq = By.CLASS_NAME, 'el-submenu'
bbfxq_num = 4

# 标本登记管理
register = By.XPATH, '/html/body/div[2]/ul/div/div/li[1]'

# 标本查询按钮
query_register = By.CLASS_NAME, 'el-button--medium'
query_register_num = 1

# 输入标本号
query_spnum = By.CLASS_NAME, 'el-input__inner'
query_spnum_num = 3

# 新增验单按钮
create_register = By.CLASS_NAME, 'el-button--medium'
create_register_num = 3

# 诊疗卡号
hospnum = By.CLASS_NAME, 'el-input__inner'
hospnum_num = 11

# 所属科室
department1 = By.CLASS_NAME, 'el-input__inner'
department1_num = 13

department2 = By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[4]'

# 主诊医生
doctor1 = By.CLASS_NAME, 'el-input__inner'
doctor1_num = 24

doctor2 = By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[4]'

# 输入检验项目
inspection = By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[4]/div/div[1]/div[1]/form/div[1]/div/div/div[1]/span/span/div/input'

# 登记保存按钮
register_save = By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/button[4]'

# 获取标本号文本
text = By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]/div'

# 标本分析中管理
bbfxz = By.CLASS_NAME, 'el-submenu'
bbfxz_num = 5

# 结果编辑管理
result = By.XPATH, '/html/body/div[2]/ul/div/div/li[1]'

# 输入标本号
spnum1 = By.CLASS_NAME, 'el-input__inner'
spnum1_num = 1

spnum2 = By.CLASS_NAME, 'el-button'
spnum2_num = 0

# 关闭第一个标签页按钮
register_clock = By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div/div[1]/div/span[2]/span'

# 结果编辑按钮
result_editing = By.CLASS_NAME, 'el-button'
result_editing_num = 5

# 结果编辑输入信息
input1 = By.CLASS_NAME, 'el-input__inner'
input1_num = 13

input2 = By.CLASS_NAME, 'el-input__inner'
input2_num = 15

input3 = By.CLASS_NAME, 'el-input__inner'
input3_num = 17

input4 = By.CLASS_NAME, 'el-input__inner'
input4_num = 19

input5 = By.CLASS_NAME, 'el-input__inner'
input5_num = 21

# 结果编辑保存按钮
result_save = By.CLASS_NAME, 'el-button'
result_save_num = 6

# 结果编辑审核按钮
result_audit1 = By.CLASS_NAME, 'el-button'
result_audit1_num = 0

result_audit2 = By.CLASS_NAME, 'el-button'
result_audit2_num = 8

result_audit3 = By.CLASS_NAME, 'el-button'
result_audit3_num = 23

# 结果编辑批准按钮
result_approve1 = By.CLASS_NAME, 'el-button'
result_approve1_num = 0

result_approve2 = By.CLASS_NAME, 'el-button'
result_approve2_num = 10

result_approve3 = By.CLASS_NAME, 'el-dialog__headerbtn'
result_approve3_num = 3

# 标本状态
result_type = By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[3]/table/tbody/tr/td[2]/div'

# 标本号
result_spnum = By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[3]/table/tbody/tr/td[5]/div'

# 微生物结果审批管理
microorganism = By.XPATH, '/html/body/div[2]/ul/div/div/li[2]'

# 输入标本号
microorganism_spnum1 = By.CLASS_NAME, 'el-input__inner'
microorganism_spnum1_num = 1

# 标本查询
microorganism_spnum2 = By.CLASS_NAME, 'el-button--medium'
microorganism_spnum2_num = 0

# 微生物结果编辑
microorganism_editing = By.CLASS_NAME, 'el-button--medium'
microorganism_editing_num = 4

# 微生物结果输入
microorganism_input = By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input'

# 微生物结果保存
microorganism_save = By.CLASS_NAME, 'el-button--medium'
microorganism_save_num = 5

# 微生物结果审核
microorganism_audit1 = By.CLASS_NAME, 'el-button--medium'
microorganism_audit1_num = 7

microorganism_audit2 = By.CLASS_NAME, 'el-message-box'
microorganism_audit2_num = 0

microorganism_audit3 = By.CLASS_NAME, 'el-button'
microorganism_audit3_num = 1

# 微生物结果批准
microorganism_approve = By.CLASS_NAME, 'el-button--medium'
microorganism_approve_num = 9

# 微生物标本状态
microorganism_type = By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div'

# 微生物标本号
microorganism_spnum = By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div'



