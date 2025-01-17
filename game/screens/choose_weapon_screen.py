import pygame
from utils.loader import load_weapons
from models.weapon import Weapon

def draw_button(screen, text, rect, font, bg_color, border_color, text_color):
    """Draws a button with text, dynamic sizing, and a border."""
    # Draw button background
    pygame.draw.rect(screen, bg_color, rect)

    # Draw button border
    pygame.draw.rect(screen, border_color, rect, 4)

    # Render and draw text
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def choose_weapon_screen(hero, screen, font, screen_width, screen_height, background_image_path):
    """Displays a screen for the player to choose a weapon."""
    # Load the background image
    background = pygame.image.load(background_image_path)
    background = pygame.transform.scale(background, (screen_width, screen_height))

    # Load weapons
    weapons = load_weapons()
    selected_weapon = None

    # Button styles
    button_padding_x = 20  # Horizontal padding around text
    button_padding_y = 15  # Vertical padding around text
    bg_color = (50, 50, 50)  # Button background color
    border_color = (200, 200, 200)  # Button border color
    text_color = (255, 255, 255)  # Button text color

    # Font for text (using a stylized game font)
    button_font = pygame.font.Font("assets/fonts/Augusta.ttf", 36)

    # Calculate button positions dynamically
    buttons = []
    start_y = screen_height // 2 - (len(weapons) * (button_font.get_height() + button_padding_y * 2 + 20)) // 2

    while selected_weapon is None:
        # Draw the background
        screen.blit(background, (0, 0))

        # Title
        title_font = pygame.font.Font("assets/fonts/Augusta.ttf", 48)
        title_text = title_font.render(f"Choisissez une arme pour {hero.name} :", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 6))
        screen.blit(title_text, title_rect)

        # Draw weapon buttons
        y_offset = start_y
        for weapon in weapons:
            text = f"{weapon['name']} (Puissance : {weapon['power']})"
            text_surface = button_font.render(text, True, text_color)
            text_width = text_surface.get_width()
            text_height = text_surface.get_height()

            # Dynamic button size based on text
            button_width = text_width + button_padding_x * 2
            button_height = text_height + button_padding_y * 2
            rect = pygame.Rect(screen_width // 2 - button_width // 2, y_offset, button_width, button_height)
            draw_button(screen, text, rect, button_font, bg_color, border_color, text_color)

            buttons.append((rect, weapon))
            y_offset += button_height + 20  # Add spacing between buttons

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, weapon in buttons:
                    if rect.collidepoint(event.pos):
                        # Create a Weapon object and equip it on the hero
                        selected_weapon = Weapon(name=weapon["name"], power=weapon["power"])
                        hero.equip_weapon(selected_weapon)
                        return
