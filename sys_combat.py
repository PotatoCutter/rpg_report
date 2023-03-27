
def player_attck(new_enemy,new_player):
    import os
    import script
    from selector_display import battle_display
    from time import sleep
    
    # print(f'{new_player.name}은 {new_enemy.name}을 공격하기로 했다.')
    selector = battle_display()
    
    
    if selector == 0:                           # 선택지: 0 == 일반공격, 1 == 마법공격, 2 == 도망가기, 3 == 개발자 공격
        new_player.attack(new_enemy)
        new_player.show_status()
        new_enemy.show_status()
        if new_enemy.get_hp() <= 0:
            new_enemy.set_death(True)
        input(script.SCRIPT_0_SYSTEM_ENTER)
    elif selector == 1:
        new_player.attack_magic(new_enemy)
        new_player.show_status()
        new_enemy.show_status()
        if new_enemy.get_hp() <= 0:
            new_enemy.set_death(True)
        input(script.SCRIPT_0_SYSTEM_ENTER)
    elif selector == 2:
        for i in range(3):
            os.system('cls') 
            os.system('clear') # 터미널 클리어
            print(f'{new_player.name}'+script.SCRIPT_1_RUN_BATTLE+('.'*i))
            sleep(i)
        exit(0)
    # elif selector == 3:
    #     print('USE\'dev_admin_pistol\'')          # 개발자용 디버그 무기 *미구현
    #     new_player.developer_weapon
    
def monster_attack(new_enemy,new_player):
    import script
    
    print(f'{new_enemy.name}의 턴')     # 몬스터의 공격
    new_enemy.attack(new_player)
    new_player.show_status()
    new_enemy.show_status()
    if new_player.hp() <= 0:
        new_player.set_death(True)
        
    input(script.SCRIPT_0_SYSTEM_ENTER)