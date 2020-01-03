boss_hp = 55
boss_dmg = 8
my_hp = 50
my_mana = 500
my_arm = 0
mana_spent = 0

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
    return mana, arm

def poison(mana, turn):
    if mana >= 173 and turn == 6:
        mana -= 173
    if turn > 0 and turn <= 6:
        dmg = 3
    return mana, dmg
    
def recharge(mana, turn):
    if mana >= 229 and turn == 5:
        mana -= 229
    if turn >= 0 and turn < 5:
        mana += 101
    return mana

# Need to figure out how many spells I need to cast to win.  add mana to mana_spent (do not undo this with Shield - mana spent is always mana spent)
# Effect spells can be started on the same turn they end
# Define my turn and boss turn, then cycle.