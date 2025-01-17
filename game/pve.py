from game.screens.choose_armor_screen import choose_armor_screen
from game.exploration import explore_zone

def pve_mode(hero, screen, font, ):
    print("\n=== Mode JcE ===")

    # Exploration et combat
    for zone in ["normal", "elite", "boss"]:
        explore_zone(hero, zone, screen, font)
        if hero.hp <= 0:
            print("Game Over!")
            return
    print("Félicitations, vous avez terminé toutes les zones !")
