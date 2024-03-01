import os

def process_links(input_file, output_file):
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        for line in fin:
            line = line.strip()
            if line.startswith('https://'):
                fout.write(line + '\n')  # If the line already starts with 'https://', keep it as is
            else:
                fout.write('http://' + line + '\n')  # If it doesn't start with 'https://', add 'http://'

# 获取程序根目录
root_dir = os.path.dirname(os.path.abspath(__file__))

# 提示用户输入要读取的文件名
input_file_name = input("请输入要读取的文件名：")

# 提示用户输入要输出的文件名
output_file_name = input("请输入要输出的文件名：")

# 构建完整的文件路径
input_file_path = os.path.join(root_dir, input_file_name)
output_file_path = os.path.join(root_dir, output_file_name)

# 处理链接并写入到输出文件中
process_links(input_file_path, output_file_path)

print("链接处理完成！")
