boss_hp = 55
boss_dmg = 8
my_hp = 50
my_mana = 500

def magic_missile(mana):
    if mana >= 53:
        mana -= 53
        dmg = 4
    return dmg, mana

def drain(mana, hp):
    if mana >= 73:
        mana -= 73
        dmg = 2
        hp += 2
    return dmg, mana, hp