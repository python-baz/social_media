from colorama import Fore
import random
import string
import time
import os
print(Fore.GREEN)

NUM_COL = 65
NUM_CHR = 30
lst_row = []
for _ in range(NUM_COL):
    rnd_num = random.randint(0, NUM_CHR)
    cnt_sps = ' ' * (NUM_CHR - rnd_num)
    rnd_wrd = random.sample(
        (string.ascii_letters + string.digits), 
        rnd_num
    )
    rnd_row = ''.join(rnd_wrd) + cnt_sps
    lst_row.append(rnd_row)

while True:
    for idx, row in enumerate(lst_row):
        cnt_sps = row.count(" ")
        cnt_sps -= 1
        if cnt_sps < 0 :
            cnt_sps = NUM_CHR
        cnt_wrd = NUM_CHR - cnt_sps
        cnt_sps = ' ' * cnt_sps
        rnd_wrd = random.sample(
            (string.ascii_letters + string.digits), 
            cnt_wrd)
        rnd_row = ''.join(rnd_wrd) + cnt_sps
        lst_row[idx] = rnd_row

    for col in zip(*lst_row):
        print(''.join(col))
    time.sleep(0.1)
    os.system('clear')
    