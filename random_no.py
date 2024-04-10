# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import random

def generate_random_numbers(start, end, count):
    numbers = list(range(start, end + 1))
    random_numbers = random.sample(numbers, count)
    random_numbers.sort()  # 对随机数字进行排序
    return random_numbers

start_number = 1
end_number = 49
select_count = 6
number_of_groups = 5

for group_number in range(1, number_of_groups + 1):
    random_numbers = generate_random_numbers(start_number, end_number, select_count)
    output = f"第{group_number}组数字: "
    for number in random_numbers:
        if number < 10:  # 判断数字是否为一位数
            output += "0"  # 添加补位的零
        output += f"{number} "
    print(output)


