import requests
import csv
from concurrent.futures import ThreadPoolExecutor
import argparse
import time

def get_status_code(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code
    except requests.RequestException:
        return "无法访问"

def process_url(url, writer):
    status_code = get_status_code(url)
    writer.writerow([url, status_code])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="指定URL文件")
    args = parser.parse_args()

    if not args.file:
        print("请指定URL文件，使用 -f 参数")
        return

    output_file = "status_codes.csv"

    with open(output_file, mode="w", encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["URL", "状态码"])

        with ThreadPoolExecutor(max_workers=10) as executor:
            with open(args.file, "r", encoding="utf-8") as file:
                urls = [line.strip() for line in file.readlines()]
                for url in urls:
                    executor.submit(process_url, url, csv_writer)

    print(f"结果已保存到 {output_file}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"总耗时: {end_time - start_time:.2f} 秒")
