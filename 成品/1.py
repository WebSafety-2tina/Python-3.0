import requests
from art import *

message = "Marco !"
# banner3 字体
banner3_art = text2art(message, font='banner3')
print("Banner3 Font:")
print(banner3_art)
print()

url = "http://ip.360.cn:80/IPQuery/ipquery"
cookies = {"crypt_code": "B02SZv%252B4s1S4mGwa5xEScQVUPO0T8d2MZjFTEgWBG%252FGblq3UEXT1h3KUmM4V3dcS"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://ip.360.cn/",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://ip.360.cn",
    "Connection": "close",
}

# 获取要查询的 IP 地址
ip_address = input("请输入要查询的 IP 地址: ")

# 构建请求数据
data = {"ip": ip_address, "verifycode": ''}

try:
    # 发送 POST 请求
    res = requests.post(url, headers=headers, cookies=cookies, data=data)
    res.raise_for_status()  # 如果请求失败，会抛出一个异常

    # 打印响应数据
    print(res.json())
except requests.RequestException as e:
    print("请求出错:", e)
input("please input any key to exit!")