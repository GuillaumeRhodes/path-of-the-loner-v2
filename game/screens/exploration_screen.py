import pygame
from utils.ui_helpers import draw_background, draw_button, draw_text_centered

def draw_exploration_screen(zone_type, screen, font, background_image_path):
    """Displays the exploration screen with a background and zone details."""
    draw_background(screen, background_image_path)  # Draw background
    draw_text_centered(screen, f"Zone : {zone_type.capitalize()}", font, (255, 255, 255), 100)
    draw_text_centered(screen, "Cliquez sur 'Continuer' pour rencontrer un monstre", font, (255, 255, 255), 200)

def draw_continue_button(screen, font):
    """Draws a 'Continue' button."""
    rect = pygame.Rect(screen.get_width() // 2 - 150, screen.get_height() - 200, 300, 70)
    return draw_button(screen, "Continuer", rect, font)
