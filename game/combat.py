from models.character import Archer
from utils.loader import choose_hero, generate_random_hero
from models.character import Mage

def combatPve(hero, monster):
    """Gère un combat PvE entre un héros et un monstre."""
    print(f"\nCombat Start! {hero.name} vs {monster.name}")

    monster.special_ability()

    while hero.hp > 0 and monster.hp > 0:
        if isinstance(hero, Archer):
            hero.attack_target(monster)
            if monster.hp <= 0:
                print(f"{monster.name} is defeated!")
                break

        else:
            monster.attack_target(hero)
            if hero.hp <= 0:
                print(f"{hero.name} is defeated!")
                break

        print(f"\n{hero.name} HP: {hero.hp}")
        print(f"{monster.name} HP: {monster.hp}")
        input("\nPress Enter to continue...")




def combatPvp(hero1, hero2):
    """Gère le combat PvP entre deux héros, où l'Archer attaque toujours en premier."""
    print(f"\nCombat Start! Player 1 ({hero1.name}) vs Player 2 ({hero2.name})")
    print(f"Player 2 starts with {hero2.hp} HP, {hero2.attack} Attack, {hero2.defense} Defense")
    print(f"Player 2 is equipped with {hero2.weapon.name} and {hero2.armor.name}")

    if isinstance(hero1, Archer):
        first, first_role = hero1, "Player 1"
        second, second_role = hero2, "Player 2"
    elif isinstance(hero2, Archer):
        first, first_role = hero2, "Player 2"
        second, second_role = hero1, "Player 1"
    else:
        first, first_role = hero1, "Player 1"
        second, second_role = hero2, "Player 2"

    print(f"\n{first_role} ({first.name}) attacks first!")

    while first.hp > 0 and second.hp > 0:
        print(f"\n{first_role} ({first.name}), it's your turn!")
        first.attack_target(second, first_role)  
        if second.hp <= 0:
            print(f"{second_role} ({second.name}) is defeated!")
            break

        print(f"\n{first_role} ({first.name}) HP: {first.hp}")
        print(f"{second_role} ({second.name}) HP: {second.hp}")
        input("\nPress Enter to continue...")

        print(f"\n{second_role} ({second.name}), it's your turn!")
        second.attack_target(first, second_role)  
        if first.hp <= 0:
            print(f"{first_role} ({first.name}) is defeated!")
            break

        print(f"\n{first_role} ({first.name}) HP: {first.hp}")
        print(f"{second_role} ({second.name}) HP: {second.hp}")
        input("\nPress Enter to continue...")






