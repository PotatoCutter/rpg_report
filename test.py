from pick import pick
import script
from time import sleep
import os


def dead_count():
    for i in range(5):
        # print(f'{new_player.name}'+script.SCRIPT_1_RUN_BATTLE+('.'*i))
        os.system('cls')  # window
        os.system('clear')  # mac, etc


s = 'rkaskvn'
sel = ['a', 'v', 'c']

selec, index = pick(sel, s)
print(index, selec)
