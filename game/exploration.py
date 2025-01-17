import random
import pygame
from models.monster import NormalMonster, EliteMonster, BossMonster
from game.combat import combatPve
from game.screens.exploration_screen import draw_exploration_screen, draw_continue_button
from utils.ui_helpers import draw_background  # Nouvelle fonction pour afficher le fond

def get_random_monster(zone_type):
    """Returns a random monster based on the zone type."""
    if zone_type == "normal":
        return random.choice([
            NormalMonster("Gobelin", 30, 5, 2, "normal"),
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
            BossMonster("Roi Démon", 120, 25, 12, "boss")
        ])

def explore_zone(hero, zone_type, screen, font):
    """Displays an exploration screen and triggers a PvE combat."""
    running = True

    # Set the background image for the zone
    background_image_path = f"assets/{zone_type}_zone.png"

    while running:
        # Draw exploration screen
        draw_exploration_screen(zone_type, screen, font, background_image_path)

        # Draw "Continue" button
        continue_button = draw_continue_button(screen, font)

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint(event.pos):
                    # Spawn a random monster
                    monster = get_random_monster(zone_type)
                    print(f"Vous rencontrez un {monster.name} !")

                    # Redraw the background before showing the monster message
                    draw_background(screen, background_image_path)

                    # Show monster encounter message
                    monster_text = font.render(f"Un {monster.name} apparaît !", True, (255, 255, 255))  # White text
                    screen.blit(monster_text, (screen.get_width() // 2 - monster_text.get_width() // 2, screen.get_height() // 2))
                    pygame.display.flip()
                    pygame.time.wait(2000)

                    # Start combat with the same background as the zone
                    combatPve(hero, monster, screen, font, background_image_path)
                    running = False
