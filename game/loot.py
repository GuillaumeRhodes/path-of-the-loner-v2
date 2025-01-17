import random
from models.equipment import Weapon, Armor

def loot(hero):
    loot_type = random.choice(["weapon", "armor"])
    
    if loot_type == "weapon":
        weapon = Weapon(f"Épée épique {random.randint(1, 10)}", random.randint(5, 15))
        print(f"Vous avez trouvé une arme : {weapon.name} (Puissance : {weapon.power}) !")
        hero.equip_weapon(weapon)
    elif loot_type == "armor":
        armor = Armor(f"Bouclier d'acier {random.randint(1, 10)}", random.randint(3, 10))
        print(f"Vous avez trouvé une armure : {armor.name} (Défense : {armor.defense}) !")
        hero.equip_armor(armor)
