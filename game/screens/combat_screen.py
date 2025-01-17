import pygame
import os
from utils.ui_helpers import draw_background, draw_button, draw_text_centered


# Chargement dynamique des images
def load_image(entity_type, entity_name):
    """
    Load an image dynamically based on the entity type ("hero" or "monster") and name.
    """
    image_path = f"assets/{entity_name.lower().replace(' ', '')}.png"
    if os.path.exists(image_path):
        return pygame.image.load(image_path)
    else:
        print(f"Image not found: {image_path}")
        return None

def draw_combat_screen(hero, monster, messages, screen, font, background_image_path, scroll_offset=0):
    """
    Displays the combat screen with a background, hero/monster images and information, and a scrollable console for messages.
    """
    # Load and display the background image
    background = pygame.image.load(background_image_path)
    background = pygame.transform.scale(background, screen.get_size())
    screen.blit(background, (0, 0))

    # Load hero and monster images
    hero_image = load_image("hero", hero.class_name)  # Accès via un attribut `class_name`
    monster_image = load_image("monster", monster.name)

    # Display hero image (if loaded)
    if hero_image:
        hero_image = pygame.transform.scale(hero_image, (300, 300))  # Resize image
        hero_image_rect = hero_image.get_rect(center=(200, screen.get_height() // 2))
        screen.blit(hero_image, hero_image_rect)

    # Display monster image (if loaded)
    if monster_image:
        monster_image = pygame.transform.scale(monster_image, (300, 300))  # Resize image
        monster_image_rect = monster_image.get_rect(center=(screen.get_width() - 200, screen.get_height() // 2))
        screen.blit(monster_image, monster_image_rect)

    # Display hero's HP closer to the hero's image
    hero_text = font.render(f"{hero.name} - HP : {hero.hp}", True, (255, 255, 255))  # White text
    hero_text_rect = hero_text.get_rect(center=(200, screen.get_height() // 2 + 200))
    screen.blit(hero_text, hero_text_rect)

    # Display monster's HP closer to the monster's image
    monster_text = font.render(f"{monster.name} - HP : {monster.hp}", True, (255, 255, 255))  # White text
    monster_text_rect = monster_text.get_rect(center=(screen.get_width() - 200, screen.get_height() // 2 + 200))
    screen.blit(monster_text, monster_text_rect)

    # Console dimensions
    console_width, console_height = 800, 400
    console_rect = pygame.Rect(
        (screen.get_width() - console_width) // 2,  # Center horizontally
        (screen.get_height() - console_height) // 2,  # Center vertically below the middle
        console_width,
        console_height
    )
    pygame.draw.rect(screen, (50, 50, 50), console_rect)  # Dark gray background
    pygame.draw.rect(screen, (200, 200, 200), console_rect, 2)  # Light gray border

    # Scrollable area inside the console
    scroll_area = console_rect.inflate(-10, -10)  # Add some padding inside the console

    # Display messages with scrolling
    visible_lines = scroll_area.height // 30  # Number of visible lines in the console
    max_offset = max(0, len(messages) - visible_lines)  # Maximum scroll offset
    y_offset = scroll_area.top

    for i in range(scroll_offset, min(len(messages), scroll_offset + visible_lines)):
        message_text = font.render(messages[i], True, (255, 255, 255))  # White text
        screen.blit(message_text, (scroll_area.left + 10, y_offset))
        y_offset += 30  # Line spacing

    return max_offset  # Return the max scroll offset for clamping in combatPve



def draw_attack_button(screen, font, is_player_turn, monster_defeated):
    """Draws the attack button if it's the player's turn."""
    if is_player_turn and not monster_defeated:
        rect = pygame.Rect(screen.get_width() // 2 - 150, screen.get_height() - 200, 300, 70)
        return draw_button(screen, "Attaquer", rect, font)

def draw_next_zone_button(screen, font, monster_defeated):
    """Draws the next zone button if the monster is defeated."""
    if monster_defeated:
        rect = pygame.Rect(screen.get_width() // 2 - 150, screen.get_height() - 200, 300, 70)
        return draw_button(screen, "Zone Suivante", rect, font)
