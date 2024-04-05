import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    # 解码二维码
    decoded_objects = decode(image)
    for obj in decoded_objects:
        # 打印二维码内容和类型
        print("Data:", obj.data)
        print("Type:", obj.type)

if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"  # 你的图片路径
    read_qr_code(image_path)
from urllib.parse import urlparse

def parse_url_from_qr_code(qr_data):
    parsed_url = urlparse(qr_data)
    print("Scheme:", parsed_url.scheme)
    print("Netloc:", parsed_url.netloc)
    print("Path:", parsed_url.path)
    print("Query:", parsed_url.query)

if __name__ == "__main__":
    qr_data = "your_qr_code_data"  # 二维码内容
    parse_url_from_qr_code(qr_data)
