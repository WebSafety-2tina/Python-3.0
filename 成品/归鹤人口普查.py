print("归人口数据库\n序列号1就是教师32w数据\n序列号3就是人口猎魔数据\n序列号4就是车主数据")
import requests
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 获取用户输入的姓名和身份证号码
name = input("请输入序列号:")
id_number = input("请输入姓名:")

# 构建URL
url = f"https://skey.live/infoSearch.php?id={name}&search={id_number}"

# 关闭SSL证书验证警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 发送请求并获取响应
response = requests.get(url, verify=False)
text = '5b2S6bmk5Lq65Y+j5pWw5o2u5bqT\n5b2S6bmk5Yi25L2c5YCS5Y2W5Zub5YWo5a624p2X77iP'
decoded_text = base64.b64decode(text).decode('utf-8')
print(decoded_text)
print(response.text)
