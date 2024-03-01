import sys
import logging
from scapy.all import *
import pandas as pd
from tabulate import tabulate
from tqdm import tqdm
import locale

# 设置本地化语言为中文
def set_locale():
    locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# 读取 PCAP 文件
def read_pcap(pcap_file):
    try:
        packets = rdpcap(pcap_file)
    except FileNotFoundError:
        logger.error(f"未找到 PCAP 文件: {pcap_file}")
        sys.exit(1)
    except Scapy_Exception as e:
        logger.error(f"读取 PCAP 文件时出错: {e}")
        sys.exit(1)
    return packets

# 提取数据包数据
def extract_packet_data(packets):
    packet_data = []

    for packet in tqdm(packets, desc="处理数据包", unit="packet"):
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto
            size = len(packet)
            packet_data.append({"源 IP": src_ip, "目的 IP": dst_ip, "协议": protocol, "大小": size})

    return pd.DataFrame(packet_data)

# 协议名称
def protocol_name(number):
    protocol_dict = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
    return protocol_dict.get(number, f"未知({number})")

# 分析数据包数据
def analyze_packet_data(df):
    total_bandwidth = df["大小"].sum()
    protocol_counts = df["协议"].value_counts(normalize=True) * 100
    protocol_counts.index = protocol_counts.index.map(protocol_name)

    ip_communication = df.groupby(["源 IP", "目的 IP"]).size().sort_values(ascending=False)
    ip_communication_percentage = ip_communication / ip_communication.sum() * 100
    ip_communication_table = pd.concat([ip_communication, ip_communication_percentage], axis=1).reset_index()
    ip_communication_table.columns = ["源 IP", "目的 IP", "计数", "百分比"]

    protocol_frequency = df["协议"].value_counts()
    protocol_frequency.index = protocol_frequency.index.map(protocol_name)

    ip_communication_protocols = df.groupby(["源 IP", "目的 IP", "协议"]).size().reset_index()
    ip_communication_protocols.columns = ["源 IP", "目的 IP", "协议", "计数"]
    ip_communication_protocols["协议"] = ip_communication_protocols["协议"].apply(protocol_name)

    # 计算每个 IP 通信对的百分比
    ip_communication_protocols["百分比"] = ip_communication_protocols.groupby(["源 IP", "目的 IP"])["计数"].apply(lambda x: x / x.sum() * 100).reset_index(drop=True)

    return total_bandwidth, protocol_counts, ip_communication_table, protocol_frequency, ip_communication_protocols

# 主函数
def main(pcap_file):
    set_locale()  # 设置本地化语言为中文
    packets = read_pcap(pcap_file)
    df = extract_packet_data(packets)
    total_bandwidth, protocol_counts, ip_communication_table, protocol_frequency, ip_communication_protocols = analyze_packet_data(df)

    logger.info(f"总带宽使用量: {total_bandwidth:.2f} 字节")
    logger.info("\n协议分布:\n")
    logger.info(tabulate(protocol_counts.reset_index(), headers=["协议", "计数", "百分比"], tablefmt="grid"))
    logger.info("\n顶级 IP 地址通信:\n")
    logger.info(tabulate(ip_communication_table, headers=["源 IP", "目的 IP", "计数", "百分比"], tablefmt="grid", floatfmt=".2f"))
    logger.info("\nIP 之间每个协议的分享情况:\n")
    logger.info(tabulate(ip_communication_protocols, headers=["源 IP", "目的 IP", "协议", "计数", "百分比"], tablefmt="grid", floatfmt=".2f"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("请提供 PCAP 文件的路径.")
        sys.exit(1)

    pcap_file = sys.argv[1]
    main(pcap_file)
