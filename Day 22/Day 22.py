boss_hp = 55
boss_dmg = 8
my_hp = 50
my_mana = 500
my_arm = 0

def magic_missile(mana):
    if mana >= 53:
        mana -= 53
        dmg = 4
    return mana, dmg

def drain(mana):
    if mana >= 73:
        mana -= 73
        dmg = 2
    return mana, dmg

def shield(mana, turn):
    if mana >= 113 and turn == 6:
        mana -= 113
    if turn > 0 and turn <= 6:
        arm = 7
        shield = True
    return mana, arm, shield

def poison(mana, turn):
    if mana >= 173 and turn == 6:
        mana -= 173
    if turn > 0 and turn <= 6:
        dmg = 3
        poison = True
    return mana, dmg, poison
    
def recharge(mana, turn):
    if mana >= 229 and turn == 5:
        mana -= 229
    if turn >= 0 and turn < 5:
        mana += 101
        recharge = True
    return mana, recharge

def combat(my_hp, my_mana, my_arm, boss_hp, boss_dmg):
    winner = 0
    mana_spent = 0
    while winner == 0:
        # My turn
        mana, dmg = magic_missile(my_mana)
        boss_hp -= dmg
        my_mana -= mana
        mana_spent += mana
        if boss_hp <= 0:
            print("You have won!")
            print("Mana spent: " + str(mana_spent))
            break
        else:
            print("You have damaged the boss for " + str(dmg) + " and his hp is now " + str(boss_hp))
        # Boss turn
        my_hp += my_arm
        my_hp -= boss_dmg
        if my_hp <= 0:
            print("You lost. :'( ")
            print("Mana spent: " + str(mana_spent))
            break
        else:
            print("The boss has damaged you for " + str(boss_dmg - my_arm) + " and your hp is now " + str(my_hp))

combat(my_hp, my_mana, my_arm, boss_hp, boss_dmg)

# Need to figure out how many spells I need to cast to win.  add mana to mana_spent (do not undo this with Shield - mana spent is always mana spent)
# Effect spells can be started on the same turn they end
# Define my turn and boss turn, then cycle.