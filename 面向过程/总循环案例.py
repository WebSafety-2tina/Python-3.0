import random
qian=10000
for i in range(1,21):
    jixiao=random.randint(1,10)
    if jixiao<5:
        print(f'员工{i}绩效分{jixiao},不满足')
        continue
    if qian>=1000:
        qian-=1000
        print(f'员工{i},满足条件，公司余额:{qian}')
    else:
        print(f'余额不足，当前余额:{qian}')
        break