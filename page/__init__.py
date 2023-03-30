from selenium.webdriver.common.by import By

# url
url = r'http://47.92.237.67/wamilis/#/login'

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

# 获取标本数量文本
text = By.CLASS_NAME, 'el-pagination__total'

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

# 关闭标本登记页按钮
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
