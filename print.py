import random

# 提供的数字（请替换为您提供的数字）
target_numbers = {14, 19, 24, 28, 31, 44}
# 随机次数计数
attempts = 0

while True:
    # 随机生成一组6个不同的数字
    random_numbers = set(random.sample(range(1, 50), 6))
    attempts += 1

    # 每100万次输出一次
    if attempts % 1_000_000 == 0:
        print(f"已尝试次数：{attempts}，当前随机结果：{random_numbers}")

    # 检查是否与目标数字相同
    if random_numbers == target_numbers:
        break

print(f"随机次数：{attempts}，成功生成的数字：{random_numbers}")