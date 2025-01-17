from tinydb import TinyDB
from models.character import Warrior, Archer, Mage
from models.equipment import Weapon, Armor
from random import choice

def choose_hero():
    db = TinyDB("data/game_data.json")
    heroes_data = db.table("heroes").all()

    print("\n=== Choix de la classe ===")
    for idx, hero in enumerate(heroes_data):
        print(f"{idx + 1}. {hero['name']} - PV: {hero['hp']}, Attaque: {hero['attack']}, Défense: {hero['defense']}")

    choice = int(input("Sélectionnez la classe que vous souhaitez jouer (1/2/3): ")) - 1
    selected_hero = heroes_data[choice]

    hero_class = globals()[selected_hero["class"]]
    return hero_class(selected_hero["name"], selected_hero["hp"], selected_hero["attack"], selected_hero["defense"])


def load_weapons():
    """Load weapons from the game data JSON file."""
    db = TinyDB("data/game_data.json")
    return db.table("weapons").all()

def load_armors():
    """Load armors from the game data JSON file."""
    db = TinyDB("data/game_data.json")
    return db.table("armors").all()


def generate_random_hero():
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
