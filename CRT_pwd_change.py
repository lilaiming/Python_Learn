# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com


import os
import re


def modify_bacth(path, pwd, username):
    files = os.listdir(path)
    for filename in files:
        pass_name = [       # 如果需要忽略某个文件夹及文件夹下的文件，在此列表中加入名字即可。
            "ISE-PAN-CNBJ.ini",
            "LenovoCppmBJ01.ini",
            "ppny019.ini",
            "ppny020.ini"
        ]
        if filename in pass_name:
            continue
        if "EAS-C2960-CNTSN04-2F" in filename:  # 排除文件名中的关键词
            continue
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            modify_bacth(filepath, pwd, username)
        elif filepath.endswith('.ini'):
            with open(filepath, 'rb') as f:
                lines = f.readlines()

            with open(filepath, 'wb') as wf:
                try:
                    for line in lines:
                        if line.decode().startswith('S:"Password V2"='):
                            line = 'S:"Password V2"=' + pwd + '\r\n'
                            wf.write(line.encode())
                        elif username and re.search(r'S\:\"Username\"\=', line.decode()):
                            line = 'S:"Username"=' + username + '\r\n'
                            wf.write(line.encode())
                        # elif 'D:"Session Password Saved"=00000000' in line.decode():  #把文件中的00000000改成00000001
                        #     line = 'D:"Session Password Saved"=00000001\r\n'
                        #     wf.write(line.encode())
                        else:
                            wf.write(line)
                except:
                    wf.writelines(lines)


def main():
    path = input("请输入需要更改的Sessions目录绝对路径：")
    username = input("请输入用户名（默认为lilm6），使用默认请回车下一步：")
    new_pwd = input("请输入加密后密码：")  # 在Sessions内查看这个新.ini文件,S:"Password V2"=后的是密码
    if not new_pwd:
        exit()
    if not username:
        username = 'lilm6'
    if not path:
        path = 'D:\OneDrive - Lenovo\SecureCRT\Sessions'  # SecureCRT 的 *.ini 文件的路径

    modify_bacth(path, new_pwd, username)


if __name__ == '__main__':
    main()








