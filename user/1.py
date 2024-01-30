import os
import requests
import re
from tqdm import tqdm
from art import text2art

# 获取脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 将 output_folder 定义在全局范围内
output_folder = os.path.join(script_dir, "mp4")
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
            # 使用绝对路径保存视频文件
            with open(video_filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        bar.update(len(chunk))

    return video_filename

def ensure_mp4_folder_exists():
    # 检查 mp4 文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def download_single_video(index=1):
    # 输入网站
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
            # 确保 mp4 文件夹存在
            ensure_mp4_folder_exists()

            # 下载视频并获取下载的文件路径
            downloaded_file = download_video(video_url, index)
            print(f"视频已下载到: {downloaded_file}")
        else:
            print("未找到视频URL。可能网页结构已更改。")

    except requests.RequestException as e:
        print(f"发生错误: {e}")

# ...（其余代码保持不变）

if __name__ == "__main__":
    main()

# 在程序结束时等待用户输入，以防控制台窗口立即关闭
input("请按任意键退出！")
