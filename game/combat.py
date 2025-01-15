from models.character import Archer
from models.character import Mage

def combatPve(hero, monster):
    """Handles PvE combat between a hero and a monster."""
    hero.role = "Joueur 1"

    print(f"\nLe combat commence! {hero.role} ({hero.name}) vs {monster.name}")

    monster.special_ability()

    while hero.hp > 0 and monster.hp > 0:
        print(f"\n{hero.role} ({hero.name}), c'est à vous d'attaquer!")
        input("\nC'est à votre tour d'attaquer, appuyez sur Entrer......")
        hero.attack_target(monster)
        if monster.hp <= 0:
            print(f"{monster.name} est battu!")
            break
        print(f"\n{hero.role} ({hero.name}) HP: {hero.hp}")
        print(f"{monster.name} HP: {monster.hp}")
        input("\nC'est au tour du Monstre d'attaquer, appuyez sur Entrer...")
        
        
        print(f"\n{monster.name} contre-attaque!")
        monster.attack_target(hero)
        if hero.hp <= 0:
            print(f"{hero.role} ({hero.name}) est battu!")
            break

        print(f"\n{hero.role} ({hero.name}) HP: {hero.hp}")
        print(f"{monster.name} HP: {monster.hp}")
        input("\nAppuyez sur Entrer pour continuer...")




def combatPvp(hero1, hero2):
    
    hero1.role = "Joueur 1"
    hero2.role = "Joueur 2"
    
    print(f"\nLe combat commence! Joueur 1 ({hero1.name}) vs Joueur 2 ({hero2.name})")
    print(f"Joueur 2 commence avec {hero2.hp} HP, {hero2.attack} d'attaque, {hero2.defense} de défense")
    print(f"Joueur 2 s'est équipé de {hero2.weapon.name} et {hero2.armor.name}")

    if isinstance(hero1, Archer):
        first, first_role = hero1, hero1.role
        second, second_role = hero2, hero2.role
    elif isinstance(hero2, Archer):
        first, first_role = hero2, hero2.role
        second, second_role = hero1, hero1.role
    else:
        first, first_role = hero1, hero1.role
        second, second_role = hero2, hero2.role

    print(f"\n{first_role} ({first.name}) attaque en premier!")

    while first.hp > 0 and second.hp > 0:
        print(f"\n{first_role} ({first.name}), c'est à vous!")
        first.attack_target(second)  
        if second.hp <= 0:
            print(f"{second_role} ({second.name}) est battu!")
            break

        print(f"\n{first_role} ({first.name}) HP: {first.hp}")
        print(f"{second_role} ({second.name}) HP: {second.hp}")
        input("\nAppuyez sur Entrer pour continuer...")

        print(f"\n{second_role} ({second.name}), c'est à vous!")
        second.attack_target(first)  
        if first.hp <= 0:
            print(f"{first_role} ({first.name}) est battu!")
            break

        print(f"\n{first_role} ({first.name}) HP: {first.hp}")
        print(f"{second_role} ({second.name}) HP: {second.hp}")
        input("\nAppuyez sur Entrer pour continuer...")






