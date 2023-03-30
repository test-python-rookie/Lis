import os

# 获取当前文件的目录
cur_path = os.path.abspath(os.path.dirname(__file__))
# 获取根目录
root_path = cur_path[:cur_path.find('Lis')]+'Lis'
join_path = r'{}/image'.format(root_path.replace('\\', '/'))
data_path = r'{}/data'.format(root_path.replace('\\', '/'))
report_path = r'{}/report'.format(root_path.replace('\\', '/'))