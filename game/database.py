from tinydb import TinyDB
from random import choice
from models.character import Warrior, Archer, Mage
from models.equipment import Weapon, Armor

def initialize_static_data():
    db = TinyDB("data/game_data.json")

    if not db.table("heroes").all():
        db.table("heroes").insert_multiple([
            {"name": "Warrior", "hp": 120, "attack": 15, "defense": 10, "class": "Warrior"},
            {"name": "Archer", "hp": 100, "attack": 18, "defense": 5, "class": "Archer"},
            {"name": "Mage", "hp": 80, "attack": 20, "defense": 3, "class": "Mage"}
        ])

    if not db.table("weapons").all():
        db.table("weapons").insert_multiple([
            {"name": "Iron Sword", "power": 10},
            {"name": "Wooden Bow", "power": 8},
            {"name": "Magic Staff", "power": 12}
        ])

    if not db.table("armors").all():
        db.table("armors").insert_multiple([
            {"name": "Leather Armor", "defense": 5},
            {"name": "Iron Shield", "defense": 7},
            {"name": "Mage Robe", "defense": 3}
        ])
    
    if not db.table("monsters").all():
        db.table("monsters").insert_multiple([
            {"name": "Goblin", "hp": 30, "attack": 5, "defense": 2, "type": "normal", "class": "NormalMonster"},
            {"name": "Slime", "hp": 25, "attack": 4, "defense": 1, "type": "normal", "class": "NormalMonster"},
            {"name": "Orc", "hp": 50, "attack": 10, "defense": 5, "type": "elite", "class": "EliteMonster"},
            {"name": "Troll", "hp": 60, "attack": 12, "defense": 6, "type": "elite", "class": "EliteMonster"},
            {"name": "Dragon", "hp": 100, "attack": 20, "defense": 10, "type": "boss", "class": "BossMonster"},
            {"name": "Demon King", "hp": 120, "attack": 25, "defense": 12, "type": "boss", "class": "BossMonster"}
        ])