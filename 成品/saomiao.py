import random

def generate_company_id(region, floor, seat, entry_date, gender, random_digit):
    # 处理输入的日期格式
    entry_date = entry_date.replace('/', '')

    # 随机生成两位年龄
    age = str(random.randint(10, 99))

    # 生成公司编号
    company_id = f"{region}{floor.zfill(2)}{seat.zfill(2)}{entry_date}{age.zfill(2)}{gender}{random_digit}"
    
    return company_id

def select_region():
    # 允许用户直接输入地区名称
    region = input("请输入地区名称: ")
    return region

# 获取地区信息
region = select_region()

# 获取一遍信息
floor = input("请输入楼层（两位数字）: ")
seat = input("请输入座位号（两位数字）: ")
entry_date = input("请输入进入公司的年月日（格式：YYYY/MMDD）: ")
gender = input("请输入性别（1表示男，0表示女）: ")
random_digit = str(random.randint(0, 9))

# 询问生成的数量
num_of_ids = int(input("请输入要生成的数量: "))

for _ in range(num_of_ids):
    # 生成不同的公司编号
    company_id = generate_company_id(region, floor, seat, entry_date, gender, random_digit)
    print("生成的公司编号:", company_id)
