from tinydb import TinyDB
from models.character import Warrior, Archer, Mage
from models.equipment import Weapon, Armor
from random import choice

def choose_hero():
    db = TinyDB("data/game_data.json")
    heroes_data = db.table("heroes").all()

    print("\n=== Choose Your Hero ===")
    for idx, hero in enumerate(heroes_data):
        print(f"{idx + 1}. {hero['name']} - HP: {hero['hp']}, Attack: {hero['attack']}, Defense: {hero['defense']}")

    choice = int(input("Select your hero (1/2/3): ")) - 1
    selected_hero = heroes_data[choice]

    hero_class = globals()[selected_hero["class"]]
    return hero_class(selected_hero["name"], selected_hero["hp"], selected_hero["attack"], selected_hero["defense"])


def choose_equipment(hero):
    db = TinyDB("data/game_data.json")

    print("\n=== Choose Your Weapon ===")
    weapons = db.table("weapons").all()
    for idx, weapon in enumerate(weapons):
        print(f"{idx + 1}. {weapon['name']} (Power: {weapon['power']})")
    weapon_choice = int(input("Select your weapon: ")) - 1
    hero.equip_weapon(Weapon(**weapons[weapon_choice]))

    print("\n=== Choose Your Armor ===")
    armors = db.table("armors").all()
    for idx, armor in enumerate(armors):
        print(f"{idx + 1}. {armor['name']} (Defense: {armor['defense']})")
    armor_choice = int(input("Select your armor: ")) - 1
    hero.equip_armor(Armor(**armors[armor_choice]))


def generate_random_hero():
    """Génère un héros aléatoire depuis TinyDB."""
    db = TinyDB("data/game_data.json")
    heroes_data = db.table("heroes").all()
    weapons_data = db.table("weapons").all()
    armors_data = db.table("armors").all()

    random_hero_data = choice(heroes_data)
    hero_class = globals()[random_hero_data["class"]]
    hero = hero_class(random_hero_data["name"], random_hero_data["hp"], random_hero_data["attack"], random_hero_data["defense"])

    random_weapon_data = choice(weapons_data)
    random_armor_data = choice(armors_data)
    weapon = Weapon(random_weapon_data["name"], random_weapon_data["power"])
    armor = Armor(random_armor_data["name"], random_armor_data["defense"])

    hero.equip_weapon(weapon)
    hero.equip_armor(armor)

    return hero
