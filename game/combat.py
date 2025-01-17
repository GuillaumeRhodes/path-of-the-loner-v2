from models.character import Archer
from models.character import Mage
import pygame
from game.constants import WHITE, BLACK
from game.screens.combat_screen import draw_combat_screen, draw_attack_button, draw_next_zone_button

def combatPve(hero, monster, screen, font, background_image_path):
    """
    Handles PvE combat between a hero and a monster with a styled background and a scrollable message console.
    """
    running = True
    player_turn = True
    messages = ["Le combat commence !"]  # Initial message
    monster_defeated = False
    last_monster_attack_time = 0  # Timing for monster's attack delay
    scroll_offset = 0  # Initial scroll position

    while running:
        # Draw the combat screen with the updated messages
        max_offset = draw_combat_screen(hero, monster, messages, screen, font, background_image_path, scroll_offset)

        # Draw buttons
        attack_button = draw_attack_button(screen, font, player_turn, monster_defeated)
        next_zone_button = draw_next_zone_button(screen, font, monster_defeated)

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if monster_defeated and next_zone_button and next_zone_button.collidepoint(event.pos):
                    messages.append("Vous passez à la zone suivante.")
                    return

                if player_turn and not monster_defeated and attack_button and attack_button.collidepoint(event.pos):
                    damage = max(0, hero.attack - monster.defense)
                    hero.attack_target(monster)
                    messages.append(f"{hero.name} inflige {damage} dégâts à {monster.name}.")
                    if hero.name == "Guerrier":
                        messages.append(f"{hero.name} inflige {damage} dégâts à {monster.name}.")

                    if monster.hp <= 0:
                        messages.append(f"Vous avez battu {monster.name} !")
                        monster_defeated = True
                        break

                    player_turn = False
                    last_monster_attack_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEWHEEL:
                # Adjust scroll offset with the mouse wheel
                scroll_offset = max(0, min(scroll_offset - event.y, max_offset))

        # Monster's turn after a delay of 2 seconds
        if not player_turn and not monster_defeated and pygame.time.get_ticks() - last_monster_attack_time >= 2000:
            damage = max(0, monster.attack - hero.defense)
            monster.attack_target(hero)
            messages.append(f"{monster.name} inflige {damage} dégâts à {hero.name}.")

            if hero.hp <= 0:
                messages.append(f"{hero.name} est battu !")
                running = False
                break

            player_turn = True






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






