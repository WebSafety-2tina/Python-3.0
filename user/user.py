import requests
import os
import threading

def download_video(i):
    url = "https://bigsofabed.com/27ed7dd9-1d67-4b41-8f5e-a0abc43c9b7e/1280x720/video{}.ts".format(i)
    root = "D://video//"
    path = root + "python{}.mp4".format(i)
    print(path)

    if not os.path.exists(root):
        os.mkdir(root)
    
    if not os.path.exists(path):
        try:
            r = requests.get(url)
            print(r.status_code)

            with open(path, 'wb') as f:
                f.write(r.content)
                print(f"文件{i}保存成功")
        except Exception as e:
            print(f"下载文件{i}失败，错误信息：{e}")
    else:
        print(f"文件{i}已存在")

try:
    # 设置线程数
    num_threads = 8

    # 创建并启动多个线程
    threads = []
    for i in range(1456):
        thread = threading.Thread(target=download_video, args=(i,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

except Exception as e:
    print(f"爬取失败，错误信息：{e}")
