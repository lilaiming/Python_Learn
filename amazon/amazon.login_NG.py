# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import requests  # 导入requests库，用于发送HTTP请求
import re  # 导入re库，用于正则表达式匹配

# 设置请求头信息

headers = {
    'Host': 'www.amazon.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
}

# 定义要访问的URL
url = "https://www.amazon.com"

# 发起GET请求，获取URL对应页面的响应结果
response = requests.get(url=url, headers=headers)

# 打印响应状态码(200成功，403禁止访问!，503服务不可用)
print(response)

# 检查是否成功获取数据
if response.status_code == 200:
    # 获取网页内容
    html_content = response.text

    # 提取标题
    title_re = r'<title>(.*?)</title>'
    title_match = re.search(title_re, html_content)
    title = title_match.group(1)
    print(title)

    # 提取登录名
    login_re = r"Hello, (.+)</span></div>"
    login_match = re.search(login_re, html_content)
    login_name = login_match.group(1)
    print(login_name)



