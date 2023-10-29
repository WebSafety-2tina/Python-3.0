import ipaddress

# 输入IP地址
ip_str = input("请输入IP地址（例如：192.168.1.0）： ")

# 输入主机位数
prefix_length = int(input("请输入主机位数（0到32之间）： "))

# 验证主机位数是否在有效范围内
if prefix_length < 0 or prefix_length > 32:
    print("无效的主机位数")
else:
    # 创建IPv4网络对象
    network = ipaddress.IPv4Network(f"{ip_str}/{prefix_length}", strict=False)

    # 获取子网掩码
    subnet_mask = network.netmask

    print(f"IP地址：{network.network_address}")
    print(f"子网掩码：{subnet_mask}")
    print(f"子网地址范围：{network.network_address} 到 {network.broadcast_address}")
    input("please input any key to exit!")