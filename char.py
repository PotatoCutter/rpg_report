from random import randint
class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """
    def __init__(self, name, hp, power):
        self.name = name            # default 값 ?
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.death = False
        

    def attack(self, other):
        damage = randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print("\n"*10+f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}\n")    
        
    
    def get_hp(self):
        return self.hp
    
    def set_death(self, death):
        self.death = death
        
    def get_death(self):
        # print(self.death)
        return self.death
    
   
class Player(Character):
    def __init__(self, name, hp,mp, power,power_magic):
        self.max_mp = mp
        self.mp = mp
        self.power_magic = power_magic
        self.skill = 1
        self.developer_weapon = 99999
        super().__init__(name,hp,power)
    
    def attack_magic(self, other):          
        damage = randint(self.power_magic - 2, self.power_magic + 2)
        other.hp = max(other.hp - damage, 0)
        self.mp = max(self.mp - self.skill , 0)
        print("\n"*10+f"{self.name}의 \"불\" 마법 공격! {other.name}에게 \"총\" 으로 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
            
    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}\n"+
              f"MP {self.mp}/{self.max_mp}\n") 
    
    # def destruction_self(self):                       # 자폭 기능 *미구현
    #     damage = (self.power_magic)
    #     self.hp = (self.hp - self.developer_weapon)       
    
class Monster(Character):
    def __init__(self, name, hp,power):
        super(Monster, self).__init__(name,hp,power)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
############################################## dead code #####################################
    
# class SpawnEntity():
#     def __init__(self, name, script):
#         self.name = name 
#         self.script = script
#         print(self.script)
        
# class CreateUser(SpawnEntity):
#     def __init__(self, name, script):
#         super(CreateUser, self).__init__(name, script)
#         return Player(name= self.name,
#                       hp = random.randint(50,200),
#                         mp=random.randint(50,200),
#                         power=random.randint(50,200),
#                         power_magic=random.randint(50,200))
        
# class CreateMonster(SpawnEntity):
#     def __init__(self, name, script):
#         super(CreateMonster, self).__init__(name, script)
#         return Monster(name= self.name,
#                         hp = random.randint(50,200),
#                         power=random.randint(50,200))
        

# class CreateUser():      
#     def __init__(self):
#         u_name = input(("\n"*10)+'당신의 이름은?\n'+('\n'*5))
#         new_player = Player(name=u_name,hp=10,mp=10,power=10,power_magic=5)
#         return new_player
        
# new_player = CreateUser(name=input(),script=script.SCRIPT_0_0_1)

        
# - 이름을 입력해 플레이어를 생성할 수 있어야 합니다.
# u_name = input(("\n"*10)+'당신의 이름은?\n'+('\n'*5))
# new_player = Player(name=input(script.SCRIPT_1_PLAYER_NAME),hp=10,mp=10,power=10,power_magic=5)
# print(f'myname{u_name}')

# - 몬스터는 임의 생성할 수 있어야 합니다.
# n_name = input(("\n"*10)+'앞에 미지의 생물이 보인다 무엇을 보았는가? \n'+('\n'*5))
# new_enemy = Monster(name=input(script.SCRIPT_1_ENEMY_NAME),hp = 20,power =20)

# new_player.attack(new_zombie)
# new_player.show_status()
# new_zombie.show_status()
# print(new_enemy.hp, new_player.hp)

# print(new_player.get_hp() == 0) # false
# print(new_enemy.hp != 0) # false


# def target(tar):

# def dice():
#     player_dice = []
#     enemy_dice = []
    
#     for i in range(3):
#         player_dice.insert(i,random.randint(1,6))
#         enemy_dice.insert(i,random.randint(1,6))
    
    
    
#     return player_dice, enemy_dice
    

# p_d, e_d = dice()
# print(max(p_d), max(e_d))


############################################################# battle page start 
# # - while 반복문을 사용해 종료 조건을 충족할 때까지 턴제 플레이어와 몬스터간 전투를 반복 진행해야 합니다.
# while new_player.get_hp() != 0 | new_enemy.get_hp() != 0 :
#     # while new_enemy.hp != 0 :
# # while False:
#     # while int(new_player.hp) != 0 & int(new_enemy.hp) != 0:
#     # new_player.attack_magic(new_enemy)
    
    
# # - 플레이어는 공격 타입을 선택할 수 있어야 합니다.
# # ['일반 공격', '마법 공격', '도망가기'] = 0, 1,2
#     if new_enemy.get_hp() <= 0 :
#         new_enemy.hp = 0
#         print(script.SCRIPT_1_DEAD_PROP)
#         input(script.SCRIPT_0_SYSTEM_ENTER)
#         # 새로운 몬스터 생성
#         # exit(0)
#     elif  new_player.get_hp() <= 0: # 체력 마이너스 방지
#         new_player.hp = 0
#         print(script.SCRIPT_1_DEAD_PLAYER)
#         input(script.SCRIPT_0_SYSTEM_ENTER)
#         exit(0)

# # ex) `일반공격` , `마법공격`
#     # print(f'{new_player.name}은 {new_enemy.name}을 공격하기로 했다.')
#     selector = battle_display()
#     if selector == 0:
#         new_player.attack(new_enemy)
#         new_player.show_status()
#         new_enemy.show_status()
#         input(script.SCRIPT_0_SYSTEM_ENTER)
#     elif selector == 1:
#         new_player.attack_magic(new_enemy)
#         new_player.show_status()
#         new_enemy.show_status()
#         input(script.SCRIPT_0_SYSTEM_ENTER)
#     elif selector == 2:
#         print(f'{new_player.name}'+script.SCRIPT_1_RUN_BATTLE)
#         # new_player.destruction_self()
#         sleep(3)
#         exit(0)
#     # elif selector == 3:
#     #     print('USE\'dev_admin_pistol\'')
#     #     new_player.developer_weapon
    
#     print(f'{new_enemy.name}의 턴')
#     new_enemy.attack(new_player)
#     input(script.SCRIPT_0_SYSTEM_ENTER)
 
 ############################################################### battle page end
        