import requests

while True:
    print("请选择操作:")
    print("1. QQ查询phone")
    print("2. LOL名称查询QQ")
    print("3. 微博查询phone")
    print("4. 退出")

    choice = input("请输入数字(1/2/3/4): ")

    if choice == '1':
        user_input = input("请输入QQ查询phone: ")
        url = f"https://zy.xywlapi.cc/qqapi?qq={user_input}"
    elif choice == '2':
        user_input = input("请输入LOL名称查询QQ: ")
        url = f"https://zy.xywlapi.cc/lolname?name={user_input}"
    elif choice == '3':
        user_input = input("请输入微博查询phone: ")
        url = f"https://zy.xywlapi.cc/wbapi?id={user_input}"
    elif choice == '4':
        print("退出程序")
        break
    else:
        print("无效选择，请输入1、2、3或4以选择操作。")
        continue

    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print("请求失败，状态码:", response.status_code)
