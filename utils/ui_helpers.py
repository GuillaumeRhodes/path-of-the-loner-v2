import pygame

def draw_background(screen, background_image_path):
    """Draws a background image on the screen."""
    background = pygame.image.load(background_image_path)
    background = pygame.transform.scale(background, screen.get_size())
    screen.blit(background, (0, 0))

def draw_button(screen, text, rect, font, bg_color=(50, 50, 50), border_color=(200, 200, 200), text_color=(255, 255, 255)):
    """Draws a styled button with text."""
    pygame.draw.rect(screen, bg_color, rect)  # Button background
    pygame.draw.rect(screen, border_color, rect, 3)  # Button border
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
    return rect

def draw_text_centered(screen, text, font, color, y):
    """Draws text centered horizontally on the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, y))
    screen.blit(text_surface, text_rect)
