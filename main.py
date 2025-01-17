import pygame
from game.database import initialize_static_data
from game.pve import pve_mode
from game.pvp import pvp_mode
from models.character import Archer, Mage, Warrior
from game.screens.main_menu_screen import main_menu_screen
from game.screens.choose_hero_screen import choose_hero_screen
from game.screens.choose_weapon_screen import choose_weapon_screen
from game.screens.choose_armor_screen import choose_armor_screen

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Path of the Loner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font("assets/fonts/Augusta.ttf", 36)  # Larger font for better readability on 1920x1080

# Main game loop
def main():
    initialize_static_data()

    while True:
        # Display the main menu
        mode = main_menu_screen(font, screen, SCREEN_WIDTH, SCREEN_HEIGHT, "assets/main_menu.png")
        
        if mode == "JcE":
            # Display the choose hero screen with the new background
            hero_class = choose_hero_screen(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, "assets/choose_hero.png")
            hero = None

            # Create the selected hero
            if hero_class == "Warrior":
                hero = Warrior(name="Guerrier", hp=120, attack=15, defense=10)
            elif hero_class == "Archer":
                hero = Archer(name="Archer", hp=100, attack=18, defense=5)
            elif hero_class == "Mage":
                hero = Mage(name="Mage", hp=80, attack=20, defense=3)

            if hero:
                choose_weapon_screen(hero, screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, "assets/choose_weapon.png")
                choose_armor_screen(hero, screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, "assets/choose_weapon.png")
                pve_mode(hero, screen, font)
        elif mode == "JcJ":
            # Start the PvP mode
            pvp_mode(screen, font)

        # End the game after finishing a mode
        print("Merci d'avoir joué!")
        pygame.quit()
        exit()

if __name__ == "__main__":
    main()
