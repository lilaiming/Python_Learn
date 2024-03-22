# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# import os
# import pytesseract
# from PIL import Image
#
# folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'output_folder')
# commands_file = '2.cfg.cmd.txt'
#
# # 设置Tesseract OCR的路径
# tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# pytesseract.pytesseract.tesseract_cmd = tesseract_path
#
# # 读取要搜索的命令列表
# commands_file_path = os.path.join(os.path.dirname(__file__), commands_file)
# with open(commands_file_path) as f:
#     search_commands = [command.strip() for command in f]
#
# def search_text_in_image(image_path):
#     # 打开图片文件
#     image = Image.open(image_path)
#
#     # 使用Tesseract OCR库提取图片中的文本
#     text = pytesseract.image_to_string(image)
#
#     return text
#
# def process_image(image_path):
#     results = []
#     text = search_text_in_image(image_path)
#     for command in search_commands:
#         occurrences = text.count(command)
#         if occurrences > 0:
#             results.extend([command] * occurrences)
#     return os.path.basename(image_path), set(results)
#
# if __name__ == '__main__':
#     # 递归遍历 output_folder 文件夹中的所有图片文件
#     image_paths = []
#     for root, dirs, files in os.walk(folder_path):
#         for filename in files:
#             if filename.endswith(('.jpg', '.jpeg', '.png')):
#                 image_path = os.path.join(root, filename)
#                 image_paths.append(image_path)
#
#     # 处理图片
#     missing_commands = {}
#     for image_path in image_paths:
#         image_name, results = process_image(image_path)
#         missing_commands[image_path] = set(search_commands) - results
#
#     # 输出包含全部命令的文件名
#     print("包含全部命令的文件名:")
#     for file_path, missing_command_set in missing_commands.items():
#         if not missing_command_set:
#             print(os.path.basename(file_path))
#
#     # 输出缺少命令的文件名
#     print("缺少命令的文件名:")
#     for file_path, missing_command_set in missing_commands.items():
#         if missing_command_set:
#             filename = os.path.basename(file_path)
#             print(f"文件 {filename} 缺少命令:")
#             for missing_command in missing_command_set:
#                 print(missing_command)

import os
import pytesseract
from PIL import Image

folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'output_folder')
commands_file = '2.cfg.cmd.txt'

# 设置Tesseract OCR的路径
tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# 读取要搜索的命令列表
commands_file_path = os.path.join(os.path.dirname(__file__), commands_file)
with open(commands_file_path) as f:
    search_commands = [command.strip() for command in f]

def search_text_in_image(image_path):
    # 打开图片文件
    image = Image.open(image_path)

    # 使用Tesseract OCR库提取图片中的文本
    text = pytesseract.image_to_string(image)

    return text

def process_image(image_path):
    results = {}
    text = search_text_in_image(image_path)
    for command in search_commands:
        occurrences = text.count(command)
        if occurrences > 0:
            results[command] = occurrences
    return os.path.basename(image_path), results

if __name__ == '__main__':
    # 递归遍历 output_folder 文件夹中的所有图片文件
    image_paths = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, filename)
                image_paths.append(image_path)

    # 处理图片
    missing_commands = {}
    for image_path in image_paths:
        image_name, results = process_image(image_path)
        missing_commands[image_path] = set(search_commands) - set(results.keys())
        print(f"文件 {image_name} 中命令出现次数:")
        for command, count in results.items():
            print(f"命令 {command}: {count} 次")

    # 输出包含全部命令的文件名
    print("包含全部命令的文件名:")
    for file_path, missing_command_set in missing_commands.items():
        if not missing_command_set:
            print(os.path.basename(file_path))

    # 输出缺少命令的文件名
    print("缺少命令的文件名:")
    for file_path, missing_command_set in missing_commands.items():
        if missing_command_set:
            filename = os.path.basename(file_path)
            print(f"文件 {filename} 缺少命令:")
            for missing_command in missing_command_set:
                print(missing_command)







