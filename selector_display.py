
def battle_display():
    from pick import pick
    scription = '당신의 턴!'
    selector = ['일반 공격', '마법 공격', '도망가기']

    index, selector = pick(selector, scription)

    return selector



###########################################################################
# from pick import pick


# def main_display():
#     scription = ''
#     selector = ['New Game', 'Quit']

#     index, selector = pick(selector, scription)

#     return selector


# print(main_display())


# def battle_display():
#     q_string = 'select your choice'
#     u_selects = ['Attack', 'Skills', 'Run', 'Dodge', 'Defense']
#     enemy = 'Earthworm'

#     select, index = pick(u_selects, q_string)

#     # print(index, select)
#     if index == 0:
#         print(f'u r a {select} to {enemy}')


############################################################################

# import keyboard

# selected = 1


# def show_menu():
#     global selected
#     print("\n" * 30)
#     print("Choose an option:")
#     for i in range(1, 5):
#         print("{1} {0}. Do something {0} {2}".format(
#             i, ">" if selected == i else " ", "<" if selected == i else " "))


# def up():
#     global selected
#     if selected == 1:
#         return
#     selected -= 1
#     show_menu()


# def down():
#     global selected
#     if selected == 4:
#         return
#     selected += 1
#     show_menu()


# show_menu()
# keyboard.add_hotkey('up', up)
# keyboard.add_hotkey('down', down)
# keyboard.wait()
