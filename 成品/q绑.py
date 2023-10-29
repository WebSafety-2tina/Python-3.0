import requests
user_input = input("请输入信息: ")
url = f"https://zy.xywlapi.cc/qqapi?qq={user_input}"
response = requests.get(url)
if response.status_code == 200:
    print(response.text)
else:
    print("请求失败，状态码:", response.status_code)
