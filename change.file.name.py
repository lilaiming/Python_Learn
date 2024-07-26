# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import os

# 定义要重命名的文件名和对应的新文件名
rename_mapping = {
    'ITVNHQSBRZ01C01': 'RZ_C01_14.1',
    'ITVNHQSBRZ11D01': 'RZ_D01_14.62',
    'ITVNHQSBRZ11D02': 'RZ_D02_14.61',
    'ITVNHQSBRZ11D03': 'RZ_D03_14.60',
}

# 指定文件所在的目录路径
root_folder = r'D:\OneDrive - Lenovo\SecureCRT\Sessions'

for folder_path, _, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith('.ini'):
            file_name, extension = os.path.splitext(filename)
            new_file_name = rename_mapping.get(file_name, file_name) + extension
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_file_name)
            os.rename(old_path, new_path)

print("文件重命名完成。")

