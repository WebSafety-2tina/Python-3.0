import requests
import re
import os
from tqdm import tqdm
from art import text2art  # 添加了art库的导入

# 将 output_folder 定义在全局范围内
output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mp4")
os.makedirs(output_folder, exist_ok=True)

# 添加message的定义
message = "Marco !"
# banner3 字体
banner3_art = text2art(message, font='banner3')
print("Banner3 Font:")
print(banner3_art)
print()

def extract_video_url(html_content):
    # 使用正则表达式提取整个视频URL
    pattern = re.compile(r'"url":\s*"(https?://[^"]+)"')
    match = pattern.search(html_content)
    if match:
        return match.group(1)
    else:
        return None

def download_video(video_url, index):
    # 获取视频文件名，使用任务编号作为文件名的一部分
    video_filename = os.path.join(output_folder, f"task_{index}_video.mp4")
    
    # 发送HTTP请求并下载视频文件
    with requests.get(video_url, stream=True) as response:
        response.raise_for_status()  # 检查是否有错误发生
        total_size = int(response.headers.get('content-length', 0))
        
        with tqdm(total=total_size, unit="B", unit_scale=True, unit_divisor=1024, bar_format='{l_bar}{bar:50}{r_bar}') as bar:
            with open(video_filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        bar.update(len(chunk))

    return video_filename

def download_single_video(index=1):
    print("注意!!!粘贴前，请确认只有视频网址，没有其他内容(原因:因为抖音复制地址后会自动复制广告)")
    print("示例:https://xxxxx.xxxxxx.com/xxxxxxxx/")
    website_url = input("请输入网站URL: ")
    
    # 构建完整的查询URL
    query_url = f"https://sy.weita.xyz/?url={website_url}"
    
    try:
        # 发送HTTP请求并获取网页内容
        response = requests.get(query_url)
        response.raise_for_status()  # 检查是否有错误发生
        
        # 提取视频URL
        video_url = extract_video_url(response.text)
        
        if video_url:
            # 下载视频并获取下载的文件路径
            downloaded_file = download_video(video_url, index)
            print(f"视频已下载到: {downloaded_file}")
        else:
            print("未找到视频URL。可能网页结构已更改。")
    
    except requests.RequestException as e:
        print(f"发生错误: {e}")

def download_single_video_from_url(url, index):
    # 构建完整的查询URL
    query_url = f"https://sy.weita.xyz/?url={url}"

    try:
        # 发送HTTP请求并获取网页内容
        response = requests.get(query_url)
        response.raise_for_status()  # 检查是否有错误发生

        # 提取视频URL
        video_url = extract_video_url(response.text)

        if video_url:
            # 下载视频并获取下载的文件路径
            downloaded_file = download_video(video_url, index)
            print(f"视频已下载到: {downloaded_file}")
        else:
            print(f"未找到视频URL，对于URL {index}。可能网页结构已更改。")

    except requests.RequestException as e:
        print(f"对于URL {index} 发生错误: {e}")

def download_multiple_videos_from_user():
    # 让用户手动输入多个URL
    print("注意!!!粘贴前，请确认只有视频网址，没有其他内容(原因:因为抖音复制地址后会自动复制广告)")
    print("示例:https://xxxxx.xxxxxx.com/xxxxxxxx/")
    urls_input = input("请输入视频地址，多个URL请用空格作为分隔分隔: ")
    urls = urls_input.split()

    # 对每个URL下载视频
    for index, url in enumerate(urls, start=1):
        url = url.strip()  # 去除首尾空白字符
        if url:
            download_single_video_from_url(url, index)

def main():
    print("抖音视频去水印下载!!!!")
    print("选择现在的方式:")
    print("1. 单个视频下载")
    print("2. 手动输入多个视频下载")
    
    choice = input("请输入选项 (1 或 2): ")
    
    if choice == '1':
        download_single_video()
    elif choice == '2':
        download_multiple_videos_from_user()
    else:
        print("无效的选项。请重新运行并输入有效的选项。")

if __name__ == "__main__":
    main()
