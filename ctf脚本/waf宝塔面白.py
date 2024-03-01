# -*- coding: utf-8 -*-
import os
import time
import threading

# 防火墙日志文件路径
LOG_FILENAME = 'log.txt'
ERROR_LOG_FILE_PATH = '/www/wwwlogs/124.220.192.251.error.log'
OTHER_LOG_FILE_PATH = '/www/wwwlogs/124.220.192.251.log'

# 检查日志文件是否存在，如果不存在则创建
if not os.path.exists(LOG_FILENAME):
    with open(LOG_FILENAME, 'w'):
        pass

# 日志文件监控线程
def tail_log_file(log_file_path, prefix):
    try:
        with open(log_file_path, "r") as file:
            while True:
                new_lines = file.readlines()
                if new_lines:
                    with open(LOG_FILENAME, "a") as log_file:
                        for line in new_lines:
                            log_file.write(f"[{prefix}] {line}")
                            print(f"[{prefix}] {line.strip()}")  # 实时显示日志内容到终端
                time.sleep(1)
    except FileNotFoundError:
        print(f"File '{log_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 启动日志文件监控线程
error_log_monitor_thread = threading.Thread(target=tail_log_file, args=(ERROR_LOG_FILE_PATH, "ERROR"), daemon=True)
error_log_monitor_thread.start()

other_log_monitor_thread = threading.Thread(target=tail_log_file, args=(OTHER_LOG_FILE_PATH, "OTHER"), daemon=True)
other_log_monitor_thread.start()

# 实时显示 log.txt 文件的内容
try:
    with open(LOG_FILENAME, "r") as log_file:
        while True:
            lines = log_file.readlines()
            if lines:
                for line in lines:
                    print(line.strip())
            time.sleep(1)
except KeyboardInterrupt:
    pass
