# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import requests  # 导入requests库，用于发送HTTP请求
import os  # 导入os库，用于文件路径操作
import re  # 导入re库，用于正则表达式匹配
import pandas as pd  # 导入pandas库，用于处理和操作数据
from datetime import datetime  # 导入datetime库，用于日期时间相关操作

# 设置请求头信息
headers = {
    'Host': 'www.amazon.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
}

# 定义要访问的URL
url = "https://www.amazon.com/Apple-iPhone-13-Pro-Sierra/dp/B0B5FLX9WS/ref=sr_1_1?crid=3H2S57WE5KP38&dib=eyJ2IjoiMSJ9.x0iwJI8EiPYwV_aSxu-DZaXO0EYEGEG69o4bTSWk6g14upXozjUBhnO1wLe9t2_8DeqBIoWZN_NyDqPfO5auPM0rVCYWgMCZ3J9n_CCGBPZZiyy6N6Xxn3PCCebO4fc6yVwQYsnfOWpEpuLb4yt1IiBvTHC0-GgygYy8wouS5ES2Al_ayieGUUq9w7vdYUsC8j6WEKW_pJuDTR9q3EObwfjJQYqElzY8tlGAv9bKh-o.MZBRsxY_2o2DUSp_4sd5e4-00NWkPZ_CtK9Lx5EZDYc&dib_tag=se&keywords=iphone%2B15%2Bpro%2Bmax&qid=1713149980&sprefix=iphone%2B15%2Bpro%2Bmax%2B%2Caps%2C331&sr=8-1&th=1"

# 发起GET请求，获取URL对应页面的响应结果
response = requests.get(url=url, headers=headers)

# 打印响应状态码(200成功，403禁止访问!，503服务不可用)
print(response)

# 检查是否成功获取数据
if response.status_code == 200:
    # 获取网页内容
    html_content = response.text

    # 获取当前日期和星期
    current_date = datetime.now()
    current_week = datetime.now().strftime("%A")
    print(current_date)
    print(current_week)

    # 提取标题
    title_re = r'<title>(.*?)</title>'
    title_match = re.search(title_re, html_content)
    title = title_match.group(1)

    Title_re = r":\s(.*?),"
    Title_match = re.search(Title_re, title)
    Title = Title_match.group(1)
    print(Title)

    # 提取价格
    price_re = r'"displayPrice":"([^"]+)"'
    price_match = re.findall(price_re, html_content)
    Price = float(price_match[0].replace('$', '').replace(',', ''))
    print(Price)

    # 提取库存数量
    stock_re = r'Only (\d+) left in stock'
    stock_match = re.findall(stock_re, html_content)
    if stock_match:
        stock = int(stock_match[0])
        print(stock)
    else:
        stock = "In Stock"
        print(stock)

    # 创建或加载现有的Excel文件
    output_folder = r"C:\Users\lilm6\Desktop\output_folder"
    output_file = os.path.join(output_folder, "amazon_test.xlsx")

    if os.path.exists(output_file):
        df = pd.read_excel(output_file)
    else:
        df = pd.DataFrame()

    if df.empty:
        last_no = 0
    else:
        last_no = df["No."].max()

    # 将新数据添加到DataFrame
    new_data = {"No.": last_no + 1, "Date": current_date, "Week": current_week, "Title":Title, "Price": Price, "Stock": stock}
    df = df._append(new_data, ignore_index=True)

    # 将DataFrame保存为Excel文件
    df.to_excel(output_file, index=False)
    print("数据保存成功。")
else:
    print("无法从URL获取数据。")

