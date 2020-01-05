import random

mana_min = 9999

def combat():
    boss_hp = 55
    boss_dmg = 8
    my_hp = 50
    mana = 500
    arm = 0
    mana_spent = 0
    spells = [['Magic Missile', 53],['Drain', 73],['Shield', 113],['Poison', 173],['Recharge', 229]]
    turn = 'Player'
    shield = False
    shield_turn = 0
    poison = False
    poison_turn = 0
    recharge = False
    recharge_turn = 0
    winner = 0

    while winner == 0:
        if shield:
            arm = 7
            shield_turn += 1
            if shield_turn == 6:
                shield = False
        else:
            arm = 0
        if poison:
            boss_hp -= 3
            if boss_hp <= 0:
                return 'You win!', mana_spent
            poison_turn += 1
            if poison_turn == 6:
                poison = False
        if recharge:
            mana += 101
            recharge_turn += 1
            if recharge_turn == 5:
                recharge = False

        if turn == 'Player':
            # Part 2
            my_hp -= 1
            if my_hp <= 0:
                return 'Boss wins. :(', mana_spent
            spell = None
            random.shuffle(spells)
            for s in spells:
                if mana >= s[1]:
                    if s[0] == 'Shield':
                        if shield:
                            continue
                    if s[0] == 'Poison':
                        if poison:
                            continue
                    if s[0] == 'Recharge':
                        if recharge:
                            continue
                    spell = s 
                    break
            if spell == None:
                return 'Boss wins. :(', mana_spent
            mana -= spell[1]
            if mana < 0:
                mana = 0
            mana_spent += spell[1]
            if spell[0] == 'Magic Missile':
                boss_hp -= 4
                if boss_hp <= 0:
                    return 'You win!', mana_spent
            if spell[0] == 'Drain':
                boss_hp -= 2
                if boss_hp <= 0:
                    return 'You win!', mana_spent
                my_hp += 2
            if spell[0] == 'Shield':
                arm = 7
                shield = True
                shield_turn = 0
            if spell[0] == 'Poison':
                poison = True
                poison_turn = 0
            if spell[0] == 'Recharge':
                recharge = True
                recharge_turn = 0
            turn = 'Boss'
        else:
            dmg = boss_dmg - arm
            if dmg < 1:
                dmg = 1
            my_hp -= dmg
            if my_hp <= 0:
                return 'Boss wins. :(', mana_spent
            turn = 'Player'

result, mana = combat()

while True:
    result, mana = combat()
    if result == 'You win!':
        if mana < mana_min:
            mana_min = mana
            print(result + " " + str(mana_min))

# Correct!  Need to stop code run after several seconds as it likely found the answer.