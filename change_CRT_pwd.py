# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import os

def modify_bacth(path, pwd, username):
    files = os.listdir(path)

    for filename in files:
        # pass_name = [
        # "ASA-Tenant-01.ini",    #排除不需要改密码的文件
        # ]
        # if filename in pass_name:
        #     continue

        if "Tenant" in filename:    # 排除关键词文件
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
                        elif username and line.decode().startswith('S:"Username"='):
                            line = 'S:"S:"Username"=' + username + '\r\n'
                            wf.write(line.encode())
                        else:
                            wf.write(line)
                except:
                    wf.writelines(lines)

def main():
    path = input("请输入需要更改的Sessions目录绝对路径：")
    username = input("请输入用户名（默认为lilm6），使用默认请回车下一步：")
    new_pwd = input("请输入加密后密码：")
    if not new_pwd:
        exit()
    if not path:
        path = 'D:\OneDrive - Lenovo\SecureCRT\Sessions'  # SecureCRT 的 *.ini 文件的路径
    modify_bacth(path, new_pwd, username)


if __name__ == '__main__':
   main()




