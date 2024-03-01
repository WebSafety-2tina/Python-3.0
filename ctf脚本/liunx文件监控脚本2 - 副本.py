import subprocess
import os
import zipfile
from datetime import datetime, timedelta

SCAN_FILE_SUFFIXES = ['.php', '.asmx', '.asp', '.aspx', '.jsp', '.jspx', '.sh', '.ashx']
SCAN_INTERVAL_MINUTES = 10
LOG_FILE = "shell.txt"
SCRIPT_PATH = os.path.abspath(__file__)

def scan_recently_modified_files():
    suffix_str = ' -o '.join('-name "*{}"'.format(suffix) for suffix in SCAN_FILE_SUFFIXES)
    command = 'find -type f \\( {} \\) -mmin -{} -not -path "{}"'.format(suffix_str, SCAN_INTERVAL_MINUTES, SCRIPT_PATH)
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.splitlines()
    except subprocess.CalledProcessError as e:
        print("扫描文件时出错: {}".format(e.output))
        return []

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            if data:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                all_data = "{} - {}\n{}\n\n".format(timestamp, file_path, data)
                append_to_log(all_data)
                remove_file(file_path)
                print("已加载文件: {}".format(file_path))
            else:
                print("文件为空: {}".format(file_path))
    except IOError:
        print("文件未找到或无法读取: {}".format(file_path))
    except Exception as e:
        print("加载文件时出错: {}".format(e))

def append_to_log(content):
    print("正在追加到日志文件: {}".format(content))
    with open(LOG_FILE, 'a+') as log_file:
        log_file.write(content)
        log_file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

def remove_file(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print("删除文件时出错: {}".format(e))

def main():
    while True:
        modified_files = scan_recently_modified_files()
        for file_path in modified_files:
            if file_path.endswith(('.zip', '.rar', '.tar.gz')):
                # 如果是压缩包文件，则记录到日志中，但不加载内容
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = "{} - {}\n压缩包文件，路径：{}\n\n".format(timestamp, file_path, file_path)
                append_to_log(log_entry)
                remove_file(file_path)
                print("已检测到压缩包文件: {}".format(file_path))
            else:
                load_file(file_path)
        time_to_sleep = timedelta(minutes=SCAN_INTERVAL_MINUTES)
        print("等待 {} 后再次扫描文件...".format(time_to_sleep))
        datetime.now() + time_to_sleep

if __name__ == '__main__':
    main()
