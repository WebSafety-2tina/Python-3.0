#!/usr/bin/python
#coding=utf-8
#2tina AWD文件保护，小型防火墙，python支持
#方式：要将此文件放在有读写权限的目录以及所有修改过的php必须在此目录或者该目录的子目录中。
#功能：读取被修改过的文件，然后将文件的地址加上内容和时间戳全部存放在txt

import subprocess
import os
from datetime import datetime, timedelta

# 定义要扫描的文件后缀和扫描文件的时间间隔
SCAN_FILE_SUFFIXES = ['.php', '.asmx', '.asp', '.aspx', '.jsp', '.jspx', '.sh','ashx']
SCAN_INTERVAL_MINUTES = 10
LOG_FILE = "shell.txt"

def scan_recently_modified_files():
    """扫描最近修改的文件"""
    suffix_str = ' -o '.join('-name "*{}"'.format(suffix) for suffix in SCAN_FILE_SUFFIXES)
    command = 'find -type f \\( {} \\) -mmin -{}'.format(suffix_str, SCAN_INTERVAL_MINUTES)
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.splitlines()
    except subprocess.CalledProcessError as e:
        print("扫描文件时出错: {}".format(e.output))
        return []

def load_file(file_path):
    """读取文件内容并记录到日志文件中"""
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
    """将内容追加到日志文件中"""
    print("正在追加到日志文件: {}".format(content))  # 调试语句
    with open(LOG_FILE, 'a+') as log_file:
        log_file.write(content)

def remove_file(file_path):
    """删除文件"""
    try:
        os.remove(file_path)
    except Exception as e:
        print("删除文件时出错: {}".format(e))
def append_to_log(content):
    """将内容追加到日志文件中"""
    print("正在追加到日志文件: {}".format(content))  # 调试语句
    with open(LOG_FILE, 'a+') as log_file:
        log_file.write(content)
        log_file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

def main():
    """主函数"""
    while True:
        modified_files = scan_recently_modified_files()
        for file_path in modified_files:
            load_file(file_path)
        # 等待一段时间再次扫描文件
        time_to_sleep = timedelta(minutes=SCAN_INTERVAL_MINUTES)
        print("等待 {} 后再次扫描文件...".format(time_to_sleep))
        datetime.now() + time_to_sleep

if __name__ == '__main__':
    main()
