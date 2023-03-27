from selenium.webdriver.common.by import By

# url
url = r'http://39.98.72.93/materialsconsume/#/login'

# 用户名
username = By.CLASS_NAME, 'el-input__inner'
name_num = 0

# 密码
password = By.CLASS_NAME, 'el-input__inner'
pwd_num = 1

# 登录按钮
login = By.CLASS_NAME, 'el-button'

# 首页
login_text = By.CLASS_NAME, 'no-redirect'
login_text_num = 0

# 入出库管理
inhouse_outhouse = By.CLASS_NAME, 'el-submenu__title'
inhouse_outhouse_num = 1

# 入库管理
inhouse = By.CLASS_NAME, 'el-menu-item'
inhouse_num = 3

# 新增入库单按钮
create_inhouse = By.CLASS_NAME, 'el-button--medium'
create_inhouse_num = 2

# 选择业务类型
business_type = By.CLASS_NAME, 'el-input__inner'
business_type_num = 8

# 选择往来单位
ealing_unit = By.CLASS_NAME, 'el-input__inner'
ealing_unit_num = 9

# 业务类型和往来单位下拉选项
pull_down1 = By.CLASS_NAME, 'el-select-dropdown__list'
pull_down1_num = 6

pull_down2 = By.CLASS_NAME, 'el-select-dropdown__item'
pull_down2_num = 1

# 选择入库物品
inhouse_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
inhouse_articles_num = 12


# 输入入库数量
inhouse_quantity = By.CLASS_NAME, 'normal-padding'
inhouse_quantity_num = 0

# 输入有效期
inhouse_today = By.CLASS_NAME, 'normal-padding'
inhouse_today_num = 7

# 新增入库单确认按钮
inhouse_confirm1 = By.CLASS_NAME, 'el-button--medium'
inhouse_confirm1_num = 6

inhouse_confirm2 = By.CLASS_NAME, 'el-message-box'
inhouse_confirm2_num = 0

inhouse_confirm3 = By.CLASS_NAME, 'el-button--primary'
inhouse_confirm3_num = 0

# 新增入库单保存按钮
inhouse_save = By.CLASS_NAME, 'el-button--medium'
inhouse_save_num = 7

# 新增入库单取消按钮
inhouse_cancel = By.CLASS_NAME, 'el-button--medium'
inhouse_cancel_num = 8

# 入库管理列表最新一条数据的录入时间
inhouse_text1 = By.CLASS_NAME, 'el-table__row'
inhouse_text1_num = 0

inhouse_text2 = By.CLASS_NAME, 'el-tooltip'
inhouse_text2_num = 0

# 请领管理
request = By.CLASS_NAME, 'el-menu-item'
request_num = 6

# 新增请领单按钮
create_request = By.CLASS_NAME, 'el-button--medium'
create_request_num = 2

# 选择请领物品
request_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
request_articles_num = 2


# 输入请领数量
request_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
request_quantity_num = 3

# 新增请领单确认按钮
request_confirm1 = By.CLASS_NAME, 'el-button--medium'
request_confirm1_num = 6

request_confirm2 = By.CLASS_NAME, 'el-message-box'
request_confirm2_num = 0

request_confirm3 = By.CLASS_NAME, 'el-button--primary'
request_confirm3_num = 0

# 新增请领单保存按钮
request_save = By.CLASS_NAME, 'el-button--medium'
request_save_num = 7

# 新增请领单取消按钮
request_cancel = By.CLASS_NAME, 'el-button--medium'
request_cancel_num = 8

# 请领管理列表最新一条数据的录入时间
request_text1 = By.CLASS_NAME, 'el-table__row'
request_text1_num = 0

request_text2 = By.CLASS_NAME, 'el-tooltip'
request_text2_num = 0

# 申领管理
agree = By.CLASS_NAME, 'el-menu-item'
agree_num = 5

# 修改申领单按钮
modify_agree = By.CLASS_NAME, 'el-button--mini'
modify_agree_num = 0

# 输入请领数量
agree_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
agree_quantity_num = 1

# 申领单确认按钮
agree_confirm1 = By.CLASS_NAME, 'el-button--medium'
agree_confirm1_num = 5

agree_confirm2 = By.CLASS_NAME, 'el-message-box'
agree_confirm2_num = 0

agree_confirm3 = By.CLASS_NAME, 'el-button--primary'
agree_confirm3_num = 0

# 申领单保存按钮
agree_save = By.CLASS_NAME, 'el-button--medium'
agree_save_num = 6

# 申领单取消按钮
agree_cancel = By.CLASS_NAME, 'el-button--medium'
agree_cancel_num = 7

# 申领单返回主表
agree_master = By.CLASS_NAME, 'el-tabs__item'
agree_master_num = 0

# 申领管理列表最新一条数据的审核时间
agree_text1 = By.CLASS_NAME, 'el-table__row'
agree_text1_num = 0

agree_text2 = By.CLASS_NAME, 'el-tooltip'
agree_text2_num = 7

# 出库管理
outhouse = By.CLASS_NAME, 'el-menu-item'
outhouse_num = 4

# 新增入库单按钮
create_outhouse = By.CLASS_NAME, 'el-button--medium'
create_outhouse_num = 2

# 选择业务类型
outhouse_business_type1 = By.CLASS_NAME, 'el-dialog__body'
outhouse_business_type1_num = 0

outhouse_business_type2 = By.CLASS_NAME, 'el-input__inner'
outhouse_business_type2_num = 0

# 选择往来单位
outhouse_ealing_unit1 = By.CLASS_NAME, 'el-dialog__body'
outhouse_ealing_unit1_num = 0

outhouse_ealing_unit2 = By.CLASS_NAME, 'el-input__inner'
outhouse_ealing_unit2_num = 1

# 业务类型和往来单位下拉选项
outhouse_pull_down1 = By.CLASS_NAME, 'el-select-dropdown__list'
outhouse_pull_down1_num = 7

outhouse_pull_down2 = By.CLASS_NAME, 'el-select-dropdown__item'
outhouse_pull_down2_num = 1

# 选择入库物品
outhouse_articles = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
outhouse_articles_num = 2

# 输入入库数量
outhouse_quantity = By.CLASS_NAME, 'tbaleInputSkipToNextOne'
outhouse_quantity_num = 3

# 修改出库单按钮
modify_outhouse = By.CLASS_NAME, 'el-button--mini'
modify_outhouse_num = 0

# 出库单确认按钮
outhouse_confirm1 = By.CLASS_NAME, 'el-button--medium'
outhouse_confirm1_num = 6

outhouse_confirm2 = By.CLASS_NAME, 'el-message-box'
outhouse_confirm2_num = 0

outhouse_confirm3 = By.CLASS_NAME, 'el-button--primary'
outhouse_confirm3_num = 0

# 出库单保存按钮
outhouse_save = By.CLASS_NAME, 'el-button--medium'
outhouse_save_num = 7

# 出库单取消按钮
outhouse_cancel = By.CLASS_NAME, 'el-button--medium'
outhouse_cancel_num = 8

# 出库管理列表最新一条数据的确认时间
outhouse_text1 = By.CLASS_NAME, 'el-table__row'
outhouse_text1_num = 0

outhouse_text2 = By.CLASS_NAME, 'el-tooltip'
outhouse_text2_num = 8