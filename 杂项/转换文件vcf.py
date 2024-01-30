import os

csv_filename = './phone.csv'

with open(csv_filename, 'r', encoding='gbk') as filename:
    f = filename.readlines()
    filename.close()
    vcards = ''

    for line in f[1:]:
        name_tel_list = line.strip().split(',')

        # 调试语句
        print("name_tel_list:", name_tel_list)

        # 检查列表长度是否足够
        if len(name_tel_list) >= 4:
            tel_name = name_tel_list[0]  # 姓名
            xing = tel_name[0]  # 姓
            ming = tel_name[1:]  # 名
            org = name_tel_list[1]  # 单位
            short_tel = name_tel_list[2]
            long_tel = name_tel_list[3]

            vcard = f'BEGIN:VCARD\nVERSION:3.0\nN:{xing};{ming};;;\nFN:{ming} {xing}\nORG:{org};\nTEL;TYPE=CELL;TYPE=pref;TYPE=VOICE:{long_tel}\nTEL;TYPE=WORK;TYPE=VOICE:{short_tel}\nPRODID:-//Apple Inc.//iCloud Web Address Book 2021B82//EN\nREV:2020-11-26T19:51:27Z\nEND:VCARD\n'

            # 调试语句
            print("Generated vCard:", vcard)

            vcards += vcard

    # 调试语句
    print("Final vcards:", vcards)

    # 保存转换后的vcf格式文件
    (fpath, temp_fname) = os.path.split(csv_filename)
    (fname, fextension) = os.path.splitext(temp_fname)

    with open(f'{fpath}{fname}_ios.vcf', "w", encoding='utf-8') as f:
        try:
            f.write(vcards)
        finally:
            f.close()
