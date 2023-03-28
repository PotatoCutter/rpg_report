import script
from time import sleep
import os


def dead_count():
    for i in range(5):
        # print(f'{new_player.name}'+script.SCRIPT_1_RUN_BATTLE+('.'*i))
        os.system('cls')  # window
        os.system('clear')  # mac, etc


# print(script)
a = input()
while True:
    print('test')
    if a == '일반공격':
        break
