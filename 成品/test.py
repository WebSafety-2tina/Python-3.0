import requests

while True:
    print("1. QQ查询phone\n2. LOL名称查询QQ\n3. 微博查询phone\n4. 退出")
    c, u = input("请输入数字(1/2/3/4): "), input("请输入QQ/LOL名称/微博: ")
    if c == '4': break
    r = requests.get(f"https://zy.xywlapi.cc/{['qqapi?qq=', 'lolname?name=', 'wbapi?id='][int(c) - 1]}{u}")
    print(r.text) if r.status_code == 200 else print(f"请求失败，状态码: {r.status_code}")
