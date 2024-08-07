# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import os
import concurrent.futures

folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'output_folder')
# folder_path = r'C:\Users\lilm6\Desktop\output_folder'
commands_file = '2.cfg.cmd.txt'

# 读取要搜索的文本列表
search_texts = []
with open(commands_file) as f:
    search_texts = [text.strip() for text in f.readlines()]

missing_commands = {}  # 缺少的命令字典，用于存储文件名和对应的缺少命令列表
all_commands = set(search_texts)  # 全部命令集合

def search_text_in_file(file_path, search_text):
    count = 0
    encodings = ['utf-8', 'latin1']  # 尝试多个编码方式
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
                count = content.count(search_text)
                if count == 0:
                    file_name = os.path.basename(file_path)  # 获取文件名
                    if file_name in missing_commands:
                        missing_commands[file_name].append(search_text)
                    else:
                        missing_commands[file_name] = [search_text]
                    all_commands.discard(search_text)
                break
        except UnicodeDecodeError:
            continue
    return count

def process_file(file_path):
    if file_path.endswith(('.txt', '.cfg', '.py', '.log')):
        for command in search_texts:
            count = search_text_in_file(file_path, command)
            if count > 0:
                file_name = os.path.basename(file_path)
                print(f"文件 {file_name} 中命令 {command} 出现了 {count} 次")

# 递归遍历文件夹中的所有文件，并使用多线程进行并行处理
with concurrent.futures.ThreadPoolExecutor() as executor:
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            executor.submit(process_file, file_path)

print("全部命令的文件名:")
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        if file_path.endswith(('.txt', '.cfg', '.py', '.log')):
            file_name = os.path.basename(file_path)
            if file_name not in missing_commands and all(command in open(file_path, encoding='utf-8').read() for command in search_texts):
                print(file_name)

print("缺少命令的文件名:")
for file_name, missing_command_list in missing_commands.items():
    print(f"文件 {file_name} 缺少命令:")
    for missing_command in missing_command_list:
        print(missing_command)

