import random

# 定义省份代码
province_codes = {
    "北京": 11,
    "天津": 12,
    "河北": 13,
    "山西": 14,
    "内蒙古": 15,
    "辽宁": 21,
    "吉林": 22,
    "黑龙江": 23,
    "上海": 31,
    "江苏": 32,
    "浙江": 33,
    "安徽": 34,
    "福建": 35,
    "江西": 36,
    "山东": 37,
    "河南": 41,
    "湖北": 42,
    "湖南": 43,
    "广东": 44,
    "广西": 45,
    "海南": 46,
    "重庆": 50,
    "四川": 51,
    "贵州": 52,
    "云南": 53,
    "西藏": 54,
    "陕西": 61,
    "甘肃": 62,
    "青海": 63,
    "宁夏": 64,
    "新疆": 65
}

# 定义出生日期
def generate_birth_date():
    year = random.randint(1900, 2003)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return year, month, day

# 定义性别
def generate_gender():
    return random.randint(1, 2)

# 定义校验码
def generate_check_code(id_number):
    id_number = id_number[:-1]
    sum = 0
    for i in range(17):
        sum += (i + 1) * id_number[i]
    check_code = (11 - sum % 11) % 10
    return str(check_code)

# 生成身份证号
def generate_id_number(province_code, city_code, district_code, birth_year, birth_month, birth_day, police_station_code, gender):
    check_code = generate_check_code(str(province_code) + str(city_code) + str(district_code) + str(birth_year) + str(birth_month) + str(birth_day) + str(gender))
    return str(province_code) + str(city_code) + str(district_code) + str(birth_year) + str(birth_month) + str(birth_day) + str(gender) + str(check_code)

# 主函数
def main():
    print("请输入以下信息：")
    province_code = input("省份序列号：")
    province = province_codes[province_code]
    city_code = input("城市序列号：")
    district_code = input("区县序列号：")
    birth_year = input("出生年份：")
    birth_month = input("出生月份：")
    birth_day = input("出生日期：")
    police_station_code = input("派出所代码：")
    gender = input("性别：")
    id_number = generate_id_number(province, city_code, district_code, birth_year, birth_month, birth_day, police_station_code, gender)
    print("生成的身份证号为：", id_number)

if __name__ == "__main__":
    main()