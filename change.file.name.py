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
    'ITVNHQSBRZ11D04': 'RZ_D04_14.59',
    'ITVNHQSBRZ11F01': 'RZ_F01_14.58',
    'ITVNHQSBRZ11F02': 'RZ_F02_14.47',
    'ITVNHQSBRZ11F03': 'RZ_F03_14.46',
    'ITVNHQSBRZ11T01': 'RZ_T01_14.57',
    'ITVNHQSBRZ11T02': 'RZ_T02_14.56',
    'ITVNHQSBRZ11T03': 'RZ_T03_14.49',
    'ITVNHQSBRZ11T04': 'RZ_T04_14.48',
    'ITVNHQSBRZ11T05': 'RZ_T05_14.53',
    'ITVNRRSBRZ11T01': 'RZ_T01_14.55',
    'ITVNHQSBSZ11D01': 'SZ_D01_14.65',
    'ITVNHQSBSZ11T01': 'SZ_T01_14.77',
    'ITVNHQSBRZCAD01': 'RZ_CAD01_14.54',
    'ANVNHQSBTZ01C01': 'TZ_C01_13.65',
    'ANVNHQSBTZ11D01': 'TZ_D01_13.126',
    'ANVNHQSBTZ11D02': 'TZ_D02_13.125',
    'ANVNHQSBTZ11F01': 'TZ_F01_13.124',
    'ANVNHQSBTZ11F02': 'TZ_F02_13.117',
    'ANVNHQSBTZ11T01': 'TZ_T01_13.123',
    'ANVNHQSBTZ11T02': 'TZ_T02_13.122',
    'ANVNHQSBTZ11T03': 'TZ_T03_13.119',
    'ANVNHQSBTZ11T04': 'TZ_T04_13.120',
    'ANVNHQSBTZ11T05': 'TZ_T05_13.113',
    'ANVNHQSBTZ11T21': 'TZ_T21_13.116',
    'ANVNHQSBTZ11T22': 'TZ_T22_13.115',
    'ANVNRRSBTZ11T01': 'TZ_T01_13.118',
    'ANVNHQSBDZ11D01': 'DZ_D01_13.200',
    'ANVNHQSBDZ11D02': 'DZ_D02_13.201',
    'ANVNHQSBDZ11M11': 'DZ_M11_13.61',
    'ANVNHQSBDZ11M21': 'DZ_M21_13.62',
    'ANVNHQSBDZ11M31': 'DZ_M31_13.60',
    'ANVNHQSBDZ11M41': 'DZ_M41_13.59',
    'ANVNHQSBUZ11D01': 'UZ_D01_13.202',
    'ANVNHQSBUZ11D02': 'UZ_D02_13.203',
    'ANVNHQSBUZ11M11': 'UZ_M11_13.26',
    'ANVNHQSBUZ11M21': 'UZ_M21_13.30',
    'ANVNHQSBUZ11M31': 'UZ_M31_13.25',
    'ANVNHQSBUZ11M41': 'UZ_M41_13.24',
    'ANVNRRSBTZCAD01': 'TZ_CAD01_13.114',
    'DEVHQSDCIRT01': 'DCI_HQS_14.105',
    'DEVNHQDCIRT01': 'DCI_NHQ_14.104',
    'ITVNHQRTRZ01': 'RTRZ01_14.50',
    'ANVNHQRTUZ01': 'RTUZ01_13.29',
    'ANVNHQRTUZ11': 'RTUZ11_13.28',
    'ANVNHQRTUZ21': 'RTUZ21_13.27',
    'ITVNHQFWSZ01': 'FWSZ01_14.67',
    'ITVNHQFWRZ01': 'FWRZ01_14.3',
    'ANVNHQFWTZ01': 'FWTZ01_13.67',
    'ANVNHQFWDT01': 'FWDT01_13.37'
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

