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

def min_equip():
    min_gold = 999
    for w in range(1, 6):
        for a in range(0, 6):
            for r1 in range(0, 7):
                for r2 in range(0, 7):
                    if r1 != r2:
                        atk, arm, gold = equip(w, a, r1, r2)
                        if atk + arm > 9 and gold < min_gold:
                            min_gold = gold
                            min_w = w
                            min_a = a
                            min_r1 = r1
                            min_r2 = r2
    return min_w, min_a, min_r1, min_r2

def max_equip():
    max_gold = 0
    for w in range(1, 6):
        for a in range(0, 6):
            for r1 in range(0, 7):
                for r2 in range(0, 7):
                    if r1 != r2:
                        atk, arm, gold = equip(w, a, r1, r2)
                        if atk + arm < 10 and gold > max_gold:
                            max_gold = gold
                            max_w = w
                            max_a = a
                            max_r1 = r1
                            max_r2 = r2
    return max_w, max_a, max_r1, max_r2

def combat(my_hp, boss_hp):
    winner = 0
    # w, a, r1, r2 = min_equip() # Part 1
    w, a, r1, r2 = max_equip() # Part 2
    my_atk, my_arm, gold = equip(w, a, r1, r2)
    boss_atk = boss_dmg - my_arm
    my_atk = my_atk - boss_arm
    # print("My Damage....." + str(max(my_atk,1)))
    # print("Boss Damage..." + str(max(boss_atk,1)))
    while winner == 0:
        boss_hp -= my_atk
        if boss_hp <= 0:
            print("You win.  Crack open a fresh Baileys!  I'm Old Gregg!!")
            print("Gold spent: " + str(gold))
            break
        my_hp -= boss_atk
        if my_hp <= 0:
            print("Boss wins.  You seen his downstairs mixup.")
            print("Gold spent: " + str(gold))
            break
    return True    

combat(my_hp, boss_hp) # Correct for Part 1 and Part 2!