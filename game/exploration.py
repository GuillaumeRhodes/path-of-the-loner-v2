import random
from models.monster import NormalMonster, EliteMonster, BossMonster
from game.combat import combatPve

def get_random_monster(zone_type):
    if zone_type == "normal":
        return random.choice([
            NormalMonster("Goblin", 30, 5, 2, "normal"),
            NormalMonster("Slime", 25, 4, 1, "normal")
        ])
    elif zone_type == "elite":
        return random.choice([
            EliteMonster("Orc", 50, 10, 5, "elite"),
            EliteMonster("Troll", 60, 12, 6, "elite")
        ])
    elif zone_type == "boss":
        return random.choice([
            BossMonster("Dragon", 100, 20, 10, "boss"),
            BossMonster("Demon King", 120, 25, 12, "boss")
        ])

def explore_zone(hero, zone_type):
    input(f"\nPress Enter to enter {zone_type.capitalize()} Zone...")
    print(f"\nEntering {zone_type.capitalize()} Zone...")
    monster = get_random_monster(zone_type)
    print(monster)
    combatPve(hero, monster)
