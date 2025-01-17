import pygame

def draw_button(screen, text, rect, color, font, text_color=(255, 255, 255)):
    """Draws a button with centered text."""
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main_menu_screen(font, screen, screen_width, screen_height, background_image_path):
    """Displays the main menu and returns the selected mode."""
    # Load the background image
    background = pygame.image.load(background_image_path)
    background = pygame.transform.scale(background, (screen_width, screen_height))

    # Button Colors
    BUTTON_COLOR = (50, 50, 50)  # Gray
    TEXT_COLOR = (255, 255, 255)  # White

    while True:
        # Draw the background image
        screen.blit(background, (0, 0))

        # Title
        title_text = font.render("=== Path of the Loner ===", True, TEXT_COLOR)
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 6))
        screen.blit(title_text, title_rect)

        # Buttons
        button_width, button_height = 400, 100
        button_spacing = 50

        start_y = screen_height // 2 - (button_height * 3 + button_spacing * 2) // 2

        pve_button = pygame.Rect(screen_width // 2 - button_width // 2, start_y, button_width, button_height)
        pvp_button = pygame.Rect(screen_width // 2 - button_width // 2, start_y + button_height + button_spacing, button_width, button_height)
        quit_button = pygame.Rect(screen_width // 2 - button_width // 2, start_y + 2 * (button_height + button_spacing), button_width, button_height)

        # Draw buttons
        draw_button(screen, "JcE (PvE)", pve_button, BUTTON_COLOR, font)
        draw_button(screen, "JcJ (PvP)", pvp_button, BUTTON_COLOR, font)
        draw_button(screen, "Quitter", quit_button, BUTTON_COLOR, font)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pve_button.collidepoint(event.pos):
                    return "JcE"
                elif pvp_button.collidepoint(event.pos):
                    return "JcJ"
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()
