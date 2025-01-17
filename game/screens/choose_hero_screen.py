import pygame

def draw_button(screen, text, rect, color, font, text_color=(255, 255, 255)):
    """Draws a button with centered text."""
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def choose_hero_screen(screen, font, screen_width, screen_height, background_image_path):
    """Displays a screen to choose a hero."""
    # Load the background image
    background = pygame.image.load(background_image_path)
    background = pygame.transform.scale(background, (screen_width, screen_height))

    # Heroes available
    heroes = [
        {"name": "Guerrier", "class": "Warrior"},
        {"name": "Archer", "class": "Archer"},
        {"name": "Mage", "class": "Mage"},
    ]
    selected_hero = None

    # Button dimensions
    button_width, button_height = 400, 100
    button_spacing = 50  # Space between buttons
    start_y = screen_height // 2 - (button_height * 3 + button_spacing * 2) // 2  # Align vertically

    while selected_hero is None:
        # Draw the background
        screen.blit(background, (0, 0))

        # Title
        title_text = font.render("Choisissez votre héros :", True, (255, 255, 255))  # White text for visibility
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 6))
        screen.blit(title_text, title_rect)

        # Buttons for heroes
        buttons = []
        for i, hero in enumerate(heroes):
            rect = pygame.Rect(screen_width // 2 - button_width // 2, start_y + i * (button_height + button_spacing), button_width, button_height)
            draw_button(screen, hero["name"], rect, (50, 50, 50), font)  # Gray background for buttons
            buttons.append((rect, hero))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, hero in buttons:
                    if rect.collidepoint(event.pos):
                        selected_hero = hero["class"]
                        return selected_hero
