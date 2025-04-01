# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import random
import time

# 提供的数字（请替换为您提供的数字）
target_numbers = {33,34,39,41,43,44}
# 随机次数计数
attempts = 0

# 记录开始时间
start_time = time.time()

while True:
    # 随机生成一组6个不同的数字
    random_numbers = set(random.sample(range(1, 50), 6))
    attempts += 1

    # 每100万次输出一次
    if attempts % 1_000_000 == 0:
        current_time = time.time()
        elapsed_time = current_time - start_time
        print(f"已尝试次数：{attempts}，当前随机结果：{random_numbers}，用时：{elapsed_time:.2f}秒")

    # 检查是否与目标数字相同
    if random_numbers == target_numbers:
        break

# 计算总用时
end_time = time.time()
total_time = end_time - start_time
print(f"随机次数：{attempts}，成功生成的数字：{random_numbers}，总用时：{total_time:.2f}秒")

