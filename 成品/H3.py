import requests
import json

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

# 定义城市代码
city_codes = {}

# 获取城市代码
def get_city_codes(province_code):
    url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2023/index.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    for item in data:
        if item["code3"] == province_code:
            city_codes[item["code2"]] = item["code1"]
    return city_codes

# 主函数
def main():
    # 获取省份列表
    province_list = list(province_codes.keys())

    # 选择省份
    province = input("请选择省份：")

    # 获取城市列表
    city_codes = get_city_codes(province_codes[province])
    city_list = list(city_codes.keys())

    # 选择城市
    city = input("请选择城市：")

    # 输出城市代码
    print("城市代码为：", city_codes[city])

if __name__ == "__main__":
    main()