import random
from models.equipment import Weapon, Armor

def loot(hero):
    loot_type = random.choice(["weapon", "armor", "gold"])
    if loot_type == "weapon":
        weapon = Weapon(f"Epic Sword {random.randint(1, 10)}", random.randint(5, 15))
        print(f"You found a weapon: {weapon.name} (Power: {weapon.power})!")
        hero.equip_weapon(weapon)
    elif loot_type == "armor":
        armor = Armor(f"Steel Shield {random.randint(1, 10)}", random.randint(3, 10))
        print(f"You found an armor: {armor.name} (Defense: {armor.defense})!")
        hero.equip_armor(armor)
    else:
        gold = random.randint(10, 50)
        print(f"You found {gold} gold coins!")
