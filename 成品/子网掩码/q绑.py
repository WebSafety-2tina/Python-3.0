import requests

while True:
    user_input = input("请输入信息: ")
    url = f"https://zy.xywlapi.cc/qqapi?qq={user_input}"

    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
        break  # 请求成功，结束循环
    elif response.status_code == 500:
        print("请求失败，状态码:", response.status_code)
        print("继续查询...")
    else:
        print("未知错误，状态码:", response.status_code)
        break  # 其他状态码，结束循环

input("请按任意键退出!")
