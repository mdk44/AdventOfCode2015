boss_hp = 100
boss_dmg = 8
boss_arm = 2
my_hp = 100
my_dmg = 0
my_arm = 0

# Item Shop array is Cost, Damage, Armor
weapons = dict()
armor = dict()
rings = dict()
weapons[1] = [8, 4, 0]
weapons[2] = [10, 5, 0]
weapons[3] = [25, 6, 0]
weapons[4] = [40, 7, 0]
weapons[5] = [74, 8, 0]
armor[1] = [13, 0, 1]
armor[2] = [31, 0, 2]
armor[3] = [53, 0, 3]
armor[4] = [75, 0, 4]
armor[5] = [102, 0, 5]
rings[1] = [25, 1, 0]
rings[2] = [50, 2, 0]
rings[3] = [100, 3, 0]
rings[4] = [20, 0, 1]
rings[5] = [40, 0, 2]
rings[6] = [80, 0, 3]

def equip(w, a, r1, r2):
    atk = my_dmg
    arm = my_arm
    gold = 0
    if w != 0:
        atk += weapons[w][1]
        gold += weapons[w][0]
    if a != 0:
        gold += armor[a][0]
        arm += armor[a][2]
    if r1 != 0:
        gold += rings[r1][0] 
        atk += rings[r1][1]
        arm += rings[r1][2]
    if r2 != 0:
        gold += rings[r2][0] 
        atk += rings[r2][1]
        arm += rings[r2][2]    
    return atk, arm, gold

def combat(my_hp, boss_hp):
    winner = 0
    my_atk, my_arm, gold = equip(1, 0, 0, 0)
    boss_atk = boss_dmg - my_arm
    my_atk = my_atk - boss_arm
    print("My Damage....." + str(max(my_atk,1)))
    print("Boss Damage..." + str(max(boss_atk,1)))
    while winner == 0:
        my_hp -= boss_atk
        if my_hp <= 0:
            print("Boss wins.  You seen his downstairs mixup.")
            print("Gold spent: " + str(gold))
            break
        boss_hp -= my_atk
        if boss_hp <= 0:
            print("You win.  Crack open a fresh Baileys!  I'm Old Gregg!!")
            print("Gold spent: " + str(gold))
            break
    return True    

#Just manually added stuff until I won for part 1
combat(my_hp, boss_hp)