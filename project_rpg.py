def main():
    import os
    import char
    import script
    from sys_combat import player_attck, monster_attack
    from random import randint, shuffle
    
    
    os.system('cls') # window 
    os.system('clear') # mac, etc               터미널 클리어
    input(script.SCRIPT_0_SYSTEM_START)
    
    gen_num = []

    for i in range(4):
        gen_num.insert(i, randint(10, 500))     # 랜덤 숫자 4개 10~ 500까지 생성

    
    new_player = char.Player(name=input(
        script.SCRIPT_1_PLAYER_NAME), hp=gen_num[0], mp=gen_num[1], power=gen_num[2], power_magic=gen_num[3])        # 캐릭터 생성
    shuffle(gen_num)            # 생성된 숫자 섞기
    new_enemy = char.Monster(name=input(                                       
        script.SCRIPT_1_ENEMY_NAME), hp=gen_num[0], power=gen_num[1])                               # 적 생성
    
    
    os.system('cls') # window 
    os.system('clear') # mac, etc               터미널 클리어
        
    print('debug')
    new_player.show_status()
    print(new_player.get_death())
    new_enemy.show_status()
    print(new_enemy.get_death())
    input()

    # while new_player.get_hp() != 0 | new_enemy.get_hp() != 0:
    while True:
        if new_player.death == False:
            if new_enemy.death == True:
                print(f'{new_enemy.name}'+script.SCRIPT_1_DEAD_PROP)
                input(script.SCRIPT_0_SYSTEM_ENTER)
                break
            player_attck(new_enemy=new_enemy, new_player=new_player)        # 고도화 이후 타겟지정 기능 추가예정
        elif new_enemy.death == False:
            if new_player.death == True:
                print(f'{new_player.name}'+script.SCRIPT_1_DEAD_PROP)
                input(script.SCRIPT_0_SYSTEM_ENTER)
                break
            monster_attack(new_enemy=new_enemy, new_player=new_player)
    exit(0)

if __name__ == "__main__":
    main()