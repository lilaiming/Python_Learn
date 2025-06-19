# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import os
import tkinter as tk
from tkinter import filedialog, messagebox
import threading


def search_files():
    folder_path = folder_var.get()
    search_text = search_var.get().strip()

    if not folder_path or not os.path.isdir(folder_path):
        messagebox.showerror("错误", "请选择有效文件夹路径")
        return
    if not search_text:
        messagebox.showerror("错误", "请输入搜索内容")
        return

    # 清空结果文本框
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "开始搜索...\n")
    result_text.update()

    # 支持的扩展名
    extensions = {'.txt', '.cfg', '.py', '.log'}
    found_count = 0

    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if any(file.lower().endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                    except UnicodeDecodeError:
                        try:
                            with open(file_path, 'r', encoding='gbk') as f:
                                lines = f.readlines()
                        except Exception as e:
                            result_text.insert(tk.END, f"无法读取文件 {file_path} ({e})\n")
                            continue
                    except Exception as e:
                        result_text.insert(tk.END, f"无法读取文件 {file_path} ({e})\n")
                        continue

                    found = False
                    for line_num, line in enumerate(lines, 1):
                        if search_text in line:
                            if not found:
                                result_text.insert(tk.END, f"\n在文件中找到匹配: {file_path}\n")
                                found = True
                                found_count += 1
                            result_text.insert(tk.END, f"  行 {line_num}: {line.strip()}\n")

        result_text.insert(tk.END, f"\n搜索完成！在 {found_count} 个文件中找到匹配内容\n")
    except Exception as e:
        messagebox.showerror("错误", f"搜索过程中出错: {str(e)}")


def select_folder():
    folder = filedialog.askdirectory(title="选择要搜索的文件夹")
    if folder:
        folder_var.set(folder)


def start_search_thread():
    threading.Thread(target=search_files, daemon=True).start()


# 创建主窗口
root = tk.Tk()
root.title("文件内容搜索工具")
root.geometry("800x600")

# 变量
folder_var = tk.StringVar()
search_var = tk.StringVar()

# 布局
tk.Label(root, text="选择文件夹:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Entry(root, textvariable=folder_var, width=50).grid(row=0, column=1, padx=5, pady=10)
tk.Button(root, text="浏览...", command=select_folder).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="搜索内容:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Entry(root, textvariable=search_var, width=50).grid(row=1, column=1, padx=5, pady=10)
tk.Button(root, text="开始搜索", command=start_search_thread, bg="#4CAF50", fg="white").grid(row=1, column=2, padx=10,
                                                                                             pady=10)

# 结果文本框
result_text = tk.Text(root, wrap="word")
result_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# 滚动条
scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.grid(row=2, column=3, sticky="ns")
result_text.config(yscrollcommand=scrollbar.set)

# 网格配置
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()


