# 从txt文件中逐行读取前7位手机号码
with open('phone.txt', 'r') as file:
    prefixes = file.readlines()

# 后2位手机号码
suffix = "06"

# 存储生成的11位手机号的列表
output_numbers = []

# 遍历每个前7位手机号，枚举中间两位数字生成完整的11位手机号
for prefix in prefixes:
    prefix = prefix.strip()  # 去除换行符等空白字符
    for i in range(0, 99):
        middle_digits = f"{i:02}"
        full_number = f"{prefix}{middle_digits}{suffix}"
        output_numbers.append(full_number)

# 将生成的11位手机号写入新的txt文件
with open('phone2.txt', 'w') as output_file:
    for number in output_numbers:
        output_file.write(f"{number}\n")
