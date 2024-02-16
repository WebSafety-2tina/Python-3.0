import time

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
