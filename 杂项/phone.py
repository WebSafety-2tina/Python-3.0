import requests
import time
from art import *

message = "Marco !"
# banner3 字体
banner3_art = text2art(message, font='banner3')
print("Banner3 Font:")
print(banner3_art)
print()
def send_api_request(api_url, params):
    try:
        response = requests.get(api_url, params=params)
        # 如果需要，你可以打印出服务器的响应内容
        print(response.text)
        return response.status_code
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    base_url = "http://guihe.23pqzn.cfd/ddps.php"

    input_data = input("请输入要提交的电话号码: ")
    num_requests = int(input("请输入要重复提交的次数: "))

    for i in range(num_requests):
        print(f"\n第{i+1}次提交：")
        params = {"phone": input_data}
        status_code = send_api_request(base_url, params)
        
        if status_code is not None:
            print(f"HTTP状态码: {status_code}")

        # 添加适当的延迟，避免过于频繁的请求
        time.sleep(1)

if __name__ == "__main__":
    main()
