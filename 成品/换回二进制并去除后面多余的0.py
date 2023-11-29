with open('bits_on_wire.txt', 'r') as r:
    bits = r.read()
bins = ''  # 存放转换后的bins
for i in range(len(bits)):

    if bits[0:2] == '10':
        bins += '1'
    else:
        bins += '0'
    bits = bits[2:]
print(bins)
print(len(bins))