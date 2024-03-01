# -*- coding: utf-8 -*-
import re
import os
import time
import threading
from datetime import datetime
# 防火墙日志文件路径
LOG_FILENAME = 'log.txt'

# 定义防火墙规则列表和相应的处理逻辑
regex_patterns = [
    (re.compile(r'\.\./\.\./'), "Directory Traversal Protection 1"),
    (re.compile(r'(?:etc\/\W*passwd)'), "Directory Traversal Protection 3"),
    (re.compile(r'(gopher|doc|php|glob|^file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/\/'), "PHP Stream Protocol Filter 1"),
    (re.compile(r'base64_decode\('), "One-Liner Backdoor Filter 3"),
    (re.compile(r'(?:define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|char|chr|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)\('), "One-Liner Backdoor Filter 4"),
    (re.compile(r'\$_(GET|post|cookie|files|session|env|phplib|GLOBALS|SERVER)\['), "One-Liner Backdoor Filter 5"),
    (re.compile(r'\s+(or|xor|and)\s+.*(=|<|>|\'|\")'), "SQL Injection Filter 1"),
    (re.compile(r'select.+(from|limit)'), "SQL Injection Filter 2"),
    (re.compile(r'(?:union(.*?)select)'), "SQL Injection Filter 3"),
    (re.compile(r'sleep\((\s*)(\d*)(\s*)\)'), "SQL Injection Filter 5"),
    (re.compile(r'benchmark\((.*)\,(.*)\)'), "SQL Injection Filter 6"),
    (re.compile(r'(?:from\W+information_schema\W)'), "SQL Injection Filter 7"),
    (re.compile(r'(?:(?:current_)user|database|concat|extractvalue|polygon|updatexml|geometrycollection|schema|multipoint|multipolygon|connection_id|linestring|multilinestring|exp|right|sleep|group_concat|load_file|benchmark|file_put_contents|urldecode|system|file_get_contents|select|substring|substr|fopen|popen|phpinfo|user|alert|scandir|shell_exec|eval|execute|concat_ws|strcmp|right)\s*\('), "SQL Injection Filter 8"),
    (re.compile(r'into(\s+)+(?:dump|out)file\s*'), "SQL Injection Filter 9"),
    (re.compile(r'group\s+by.+'), "SQL Injection Filter 10"),
    (re.compile(r'(invokefunction|call_user_func_array|\\\\think\\\\)'), "ThinkPHP Payload Block"),
    (re.compile(r'^url_array\[.*\]$'), "Metinfo6.x XSS Vulnerability"),
    (re.compile(r'(extractvalue\(|concat\(0x|user\(\)|substring\(|count\(\*\)|substring\(hex\(|updatexml\()'), "SQL Error-Based Injection Filter 01"),
    (re.compile(r'(@@version|load_file\(|NAME_CONST\(|exp\(\~|floor\(rand\(|geometrycollection\(|multipoint\(|polygon\(|multipolygon\(|linestring\(|multilinestring\()'), "SQL Error-Based Injection Filter 02"),
    (re.compile(r'(substr\()'), "SQL Injection Filter 10"),
    (re.compile(r'(ORD\(|MID\(|IFNULL\(|CAST\(|CHAR\()'), "SQL Injection Filter 1"),
    (re.compile(r'(EXISTS\(|SELECT\#|\(SELECT)'), "SQL Injection Filter 1"),
    (re.compile(r'(bin\(|ascii\(|benchmark\(|concat_ws\(|group_concat\(|strcmp\(|left\(|datadir\(|greatest\()'), "SQL Error-Based Injection Filter 01"),
    (re.compile(r'(?:from.+?information_schema.+?)'), ""),
    (re.compile(r'(array_map\("ass)'), "Cknife Traffic Filter"),
    (re.compile(r'(HTTrack|antSword|harvest|audit|dirbuster|pangolin|nmap|sqln|hydra|Parser|libwww|BBBike|sqlmap|w3af|owasp|Nikto|fimap|havij|zmeu|BabyKrokodil|netsparker|httperf| SF/)'), "Keyword Filter 1"),
    (re.compile(r'(gopher|doc|php|glob|file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/\/'), "PHP Stream Protocol Filter 1"),
    (re.compile(r'base64_decode\('), "One-Liner *Blocked Keyword* Filter 1"),
    (re.compile(r'(?:define|eval|file_get_contents|include|require_once|shell_exec|phpinfo|system|passthru|chr|char|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog|file_put_contents|fopen|urldecode|scandir)\('), "One-Liner *Blocked Keyword* Filter 2"),
    (re.compile(r'\$_(GET|post|cookie|files|session|env|phplib|GLOBALS|SERVER)'), "One-Liner *Blocked Keyword* Filter 3"),
    (re.compile(r'select\s+.+(from|limit)\s+'), "SQL Injection Filter 2"),
    (re.compile(r'(?:union(.*?)select)'), "SQL Injection Filter 3"),
    (re.compile(r'benchmark\((.*)\,(.*)\)'), "SQL Injection Filter 6"),
    (re.compile(r'(?:from\W+information_schema\W)'), "SQL Injection Filter 7"),
    (re.compile(r'(?:(?:current_)user|database|schema|connection_id)\s*\('), "SQL Injection Filter 8"),
    (re.compile(r'into(\s+)+(?:dump|out)file\s*'), "SQL Injection Filter 9"),
    (re.compile(r'group\s+by.+'), "SQL Injection Filter 10"),
    (re.compile(r'(extractvalue\(|concat\(|user\(\)|substring\(|count\(\*\)|substring\(hex\(|updatexml\))'), "SQL Error-Based Injection Filter 01"),
    (re.compile(r'(@@version|load_file\(|NAME_CONST\(|exp\(\~|floor\(rand\(|geometrycollection\(|multipoint\(|polygon\(|multipolygon\(|linestring\(|multilinestring\(|right\()'), "SQL Error-Based Injection Filter 02"),
    (re.compile(r'(substr\()'), "SQL Injection Filter 10"),
    (re.compile(r'(ORD\(|MID\(|IFNULL\(|CAST\(|CHAR\()'), "SQL Injection Filter 1"),
    (re.compile(r'(EXISTS\(|SELECT\#|\(SELECT|select\()'), "SQL Injection Filter 1"),
    (re.compile(r'(array_map\("ass)'), "Cknife Traffic Filter"),
    (re.compile(r'(bin\(|ascii\(|benchmark\(|concat_ws\(|group_concat\(|strcmp\(|left\(|datadir\(|greatest\()'), "SQL Error-Based Injection Filter 01"),
    (re.compile(r'\.(htaccess|mysql_history|bash_history|DS_Store|idea|user\.ini)'), "File Directory Filter 1"),
    (re.compile(r'\.(bak|inc|old|mdb|sql|php~|swp|java|class)$'), "File Directory Filter 2"),
    (re.compile(r'^/(vhost|bbs|host|wwwroot|www|site|root|backup|data|ftp|db|admin|website|web).*\.(rar|sql|zip|tar\.gz|tar)$'), "File Directory Filter 3"),
    (re.compile(r'/(hack|shell|spy|phpspy)\.php$'), "PHP Script Execution Filter 1"),
    (re.compile(r'^/(attachments|css|uploadfiles|static|forumdata|cache|avatar)/(\w+)\.(php|jsp)$'), "PHP Script Execution Filter 2"),
]

# 处理匹配到的模式
def handle_matched_pattern(description):
    print(f"Matched pattern: {description}")
    # 在这里执行相应的防火墙操作，例如记录日志、拦截请求等

# 测试输入字符串是否匹配任何正则表达式
def test_regex(input_str):
    for pattern, description in regex_patterns:
        if pattern.search(input_str):
            handle_matched_pattern(description)

# 日志文件监控线程
def tail_log_file(log_file_path):
    try:
        with open(log_file_path, "r") as file:
            while True:
                new_lines = file.readlines()
                if new_lines:
                    for line in new_lines:
                        print(line.strip())
                time.sleep(1)
    except FileNotFoundError:
        print(f"File '{log_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 启动日志文件监控线程
log_monitor_thread = threading.Thread(target=tail_log_file, args=(LOG_FILENAME,), daemon=True)
log_monitor_thread.start()
# 删除特定的请求头信息
if 'accept' in header:
    del header['accept']

# 测试示例输入
test_input = "/wwwroot/test.php"
test_regex(test_input)

# 第一个文件的内容
# 定义日志文件路径
LOG_FILENAME = 'log.txt'

# 获取所有的请求头信息
def get_all_headers():
    headers = {}
    for name, value in os.environ.items():
        if name.startswith('HTTP_'):
            headers[name[5:].lower().replace('_', '-')] = value
    return headers

# 实现防火墙功能
def waf():
    # 获取请求参数
    get = os.environ.get('QUERY_STRING', {})
    post = os.environ.get('wsgi.input', {})
    cookie = os.environ.get('HTTP_COOKIE', {})
    header = get_all_headers()
    files = os.environ.get('wsgi.file_wrapper', {})
    ip = os.environ.get('REMOTE_ADDR', {})
    method = os.environ.get('REQUEST_METHOD', {})
    filepath = os.environ.get('SCRIPT_NAME', {})
    
    # 处理上传的文件
    for key, value in files:
        content = value.read()
        value.write(b"virink")
    
    # 删除特定的请求头信息
    del header['accept']
    
    # 组装输入参数
    input_params = {
        "Get": get,
        "Post": post,
        "Cookie": cookie,
        "Files": files,
        "Header": header
    }
    
    # 检查恶意模式并记录日志
    pattern = r'select|insert|update|delete|and|or|\'|\/\*|\*|\.\.\/|\.\/|union|into|load_file|outfile|dumpfile|sub|hex'
    pattern += r'|file_put_contents|fwrite|curl|system|eval|assert'
    pattern += r'|passthru|exec|system|chroot|scandir|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore'
    pattern += r'|`|dl|openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|assert|pcntl_exec'
    pattern = re.compile(pattern, re.I)
    
    for k, v in input_params.items():
        for key, value in v:
            if pattern.search(value):
                logging(input_params)
                break

# 记录日志
def logging(input_params):
    with open(LOG_FILENAME, "a") as file:
        file.write("\n\n\n")
        file.write(str(datetime.now()))
        file.write("\n")
        file.write(str(input_params))

# 在这里可以添加其他防火墙功能

# 调用防火墙函数
waf()