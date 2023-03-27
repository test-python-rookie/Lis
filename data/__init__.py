import os
from os import listdir
# 获取当前文件的目录
cur_path = os.path.abspath(os.path.dirname(__file__))
# 获取根目录
root_path = cur_path[:cur_path.find('MaterialsConsume')]+'MaterialsConsume'
join_path = r'{}/image'.format(root_path.replace('\\', '/'))