import re
import time
# 定义正则表达式列表和相应的处理逻辑
regex_patterns = [
    (re.compile(r'\.\./\.\./'), "目录保护1"),
    (re.compile(r'(?:etc\/\W*passwd)'), "目录保护3"),
    (re.compile(r'(gopher|doc|php|glob|^file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/\/'), "PHP流协议过滤1"),
    (re.compile(r'base64_decode\('), "一句话木马过滤3"),
    (re.compile(r'(?:define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|char|chr|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)\('), "一句话木马过滤4"),
    (re.compile(r'\$_(GET|post|cookie|files|session|env|phplib|GLOBALS|SERVER)\['), "一句话木马过滤5"),
    (re.compile(r'\s+(or|xor|and)\s+.*(=|<|>|\'|\")'), "SQL注入过滤1"),
    (re.compile(r'select.+(from|limit)'), "SQL注入过滤2"),
    (re.compile(r'(?:union(.*?)select)'), "SQL注入过滤3"),
    (re.compile(r'sleep\((\s*)(\d*)(\s*)\)'), "SQL注入过滤5"),
    (re.compile(r'benchmark\((.*)\,(.*)\)'), "SQL注入过滤6"),
    (re.compile(r'(?:from\W+information_schema\W)'), "SQL注入过滤7"),
    (re.compile(r'(?:(?:current_)user|database|concat|extractvalue|polygon|updatexml|geometrycollection|schema|multipoint|multipolygon|connection_id|linestring|multilinestring|exp|right|sleep|group_concat|load_file|benchmark|file_put_contents|urldecode|system|file_get_contents|select|substring|substr|fopen|popen|phpinfo|user|alert|scandir|shell_exec|eval|execute|concat_ws|strcmp|right)\s*\('), "SQL注入过滤8"),
    (re.compile(r'into(\s+)+(?:dump|out)file\s*'), "SQL注入过滤9"),
    (re.compile(r'group\s+by.+'), "SQL注入过滤10"),
    (re.compile(r'(invokefunction|call_user_func_array|\\\\think\\\\)'), "ThinkPHP payload封堵"),
    (re.compile(r'^url_array\[.*\]$'), "Metinfo6.x XSS漏洞"),
    (re.compile(r'(extractvalue\(|concat\(0x|user\(\)|substring\(|count\(\*\)|substring\(hex\(|updatexml\()'), "SQL报错注入过滤01"),
    (re.compile(r'(@@version|load_file\(|NAME_CONST\(|exp\(\~|floor\(rand\(|geometrycollection\(|multipoint\(|polygon\(|multipolygon\(|linestring\(|multilinestring\()'), "SQL报错注入过滤02"),
    (re.compile(r'(substr\()'), "SQL注入过滤10"),
    (re.compile(r'(ORD\(|MID\(|IFNULL\(|CAST\(|CHAR\()'), "SQL注入过滤1"),
    (re.compile(r'(EXISTS\(|SELECT\#|\(SELECT)'), "SQL注入过滤1"),
    (re.compile(r'(bin\(|ascii\(|benchmark\(|concat_ws\(|group_concat\(|strcmp\(|left\(|datadir\(|greatest\()'), "SQL报错注入过滤01"),
    (re.compile(r'(?:from.+?information_schema.+?)'), ""),
    (re.compile(r'(array_map\("ass)'), "菜刀流量过滤"),
    (re.compile(r'(HTTrack|antSword|harvest|audit|dirbuster|pangolin|nmap|sqln|hydra|Parser|libwww|BBBike|sqlmap|w3af|owasp|Nikto|fimap|havij|zmeu|BabyKrokodil|netsparker|httperf| SF/)'), "关键词过滤1"),
    (re.compile(r'(gopher|doc|php|glob|file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/\/'), "PHP流协议过滤1"),
    (re.compile(r'base64_decode\('), "一句话*屏蔽的关键字*过滤1"),
    (re.compile(r'(?:define|eval|file_get_contents|include|require_once|shell_exec|phpinfo|system|passthru|chr|char|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog|file_put_contents|fopen|urldecode|scandir)\('), "一句话*屏蔽的关键字*过滤2"),
    (re.compile(r'\$_(GET|post|cookie|files|session|env|phplib|GLOBALS|SERVER)'), "一句话*屏蔽的关键字*过滤3"),
    (re.compile(r'select\s+.+(from|limit)\s+'), "SQL注入过滤2"),
    (re.compile(r'(?:union(.*?)select)'), "SQL注入过滤3"),
    (re.compile(r'benchmark\((.*)\,(.*)\)'), "SQL注入过滤6"),
    (re.compile(r'(?:from\W+information_schema\W)'), "SQL注入过滤7"),
    (re.compile(r'(?:(?:current_)user|database|schema|connection_id)\s*\('), "SQL注入过滤8"),
    (re.compile(r'into(\s+)+(?:dump|out)file\s*'), "SQL注入过滤9"),
    (re.compile(r'group\s+by.+'), "SQL注入过滤10"),
    (re.compile(r'(extractvalue\(|concat\(|user\(\)|substring\(|count\(\*\)|substring\(hex\(|updatexml\))'), "SQL报错注入过滤01"),
    (re.compile(r'(@@version|load_file\(|NAME_CONST\(|exp\(\~|floor\(rand\(|geometrycollection\(|multipoint\(|polygon\(|multipolygon\(|linestring\(|multilinestring\(|right\()'), "SQL报错注入过滤02"),
    (re.compile(r'(substr\()'), "SQL注入过滤10"),
    (re.compile(r'(ORD\(|MID\(|IFNULL\(|CAST\(|CHAR\()'), "SQL注入过滤1"),
    (re.compile(r'(EXISTS\(|SELECT\#|\(SELECT|select\()'), "SQL注入过滤1"),
    (re.compile(r'(array_map\("ass)'), "菜刀流量过滤"),
    (re.compile(r'(bin\(|ascii\(|benchmark\(|concat_ws\(|group_concat\(|strcmp\(|left\(|datadir\(|greatest\()'), "SQL报错注入过滤01"),
    (re.compile(r'\.(htaccess|mysql_history|bash_history|DS_Store|idea|user\.ini)'), "文件目录过滤1"),
    (re.compile(r'\.(bak|inc|old|mdb|sql|php~|swp|java|class)$'), "文件目录过滤2"),
    (re.compile(r'^/(vhost|bbs|host|wwwroot|www|site|root|backup|data|ftp|db|admin|website|web).*\.(rar|sql|zip|tar\.gz|tar)$'), "文件目录过滤3"),
    (re.compile(r'/(hack|shell|spy|phpspy)\.php$'), "PHP脚本执行过滤1"),
    (re.compile(r'^/(attachments|css|uploadfiles|static|forumdata|cache|avatar)/(\w+)\.(php|jsp)$'), "PHP脚本执行过滤2"),
    (re.compile(r'(?:union(.*?)select)'), "SQL注入过滤1"),
    (re.compile(r'(?:define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)\('), "一句话木马过滤1"),
]

# 处理匹配到的模式
def handle_matched_pattern(description):
    print(f"发现匹配的模式：{description}")
    # 在这里执行相应的服务器保护操作，例如禁止访问、记录日志等

# 测试输入字符串是否匹配任何正则表达式
def test_regex(input_str):
    for pattern, description in regex_patterns:
        if pattern.search(input_str):
            handle_matched_pattern(description)
# 读取日志文件的路径
log_file_path = "/www/wwwlogs/124.220.192.251.log"

# 实时输出日志文件的内容
def tail_log_file(log_file_path):
    try:
        with open(log_file_path, "r") as file:
            while True:
                # 读取新添加的内容
                new_lines = file.readlines()
                if new_lines:
                    for line in new_lines:
                        print(line.strip())
                time.sleep(1)  # 每秒检查一次文件是否有新内容
    except FileNotFoundError:
        print(f"File '{log_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 启动实时输出
tail_log_file(log_file_path)
# 测试示例
test_input = "/wwwroot/test.php"
test_regex(test_input)
