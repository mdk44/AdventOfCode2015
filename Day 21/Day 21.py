boss_hp = 100
boss_dmg = 8
boss_arm = 2
my_hp = 100
my_dmg = 0
my_arm = 0

# Item Shop array is Cost, Damage, Armor and T/F (True = item stats are added to your stats and gold spent adds up)
weapons = dict()
armor = dict()
rings = dict()
weapons[0] = [8, 4, 0, False]
weapons[1] = [10, 5, 0, False]
weapons[2] = [25, 6, 0, False]
weapons[3] = [40, 7, 0, False]
weapons[4] = [74, 8, 0, False]
armor[0] = [13, 0, 1, False]
armor[1] = [31, 0, 2, False]
armor[2] = [53, 0, 3, False]
armor[3] = [75, 0, 4, False]
armor[4] = [102, 0, 5, False]
rings[0] = [25, 1, 0, False]
rings[1] = [50, 2, 0, False]
rings[2] = [100, 3, 0, False]
rings[3] = [20, 0, 1, False]
rings[4] = [40, 0, 2, False]
rings[5] = [80, 0, 3, False]

def combat(my_hp, boss_hp):
    winner = 0
    my_atk = 0
    boss_atk = 0
    my_atk = max(1, my_dmg - boss_arm)
    boss_atk = max(1, boss_dmg - my_arm)
    print("My Damage....." + str(my_atk))
    print("My Armor......" + str(my_arm))
    print("Boss Damage..." + str(boss_atk))
    print("Boss Armor...." + str(boss_arm))
    while winner == 0:
        my_hp -= boss_atk
        if my_hp <= 0:
            print("Boss wins.  You seen his downstairs mixup.")
            break
        boss_hp -= my_atk
        if boss_hp <= 0:
            print("You win.  Crack open a fresh Baileys!  I'm Old Gregg!!")
            break
    return True


for i in range(0, len(weapons)):
    if weapons[i][3] == True:
        my_dmg += weapons[i][1]
for i in range(0, len(armor)):
    if armor[i][3] == True:
        my_arm += armor[i][2]
for i in range(0, len(rings)):
    if rings[i][3] == True:
        my_dmg += rings[i][1]
        my_arm += rings[i][2]

combat(my_hp, boss_hp)