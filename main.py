from game.menu import main_menu
from game.pve import pve_mode
from game.pvp import pvp_mode
from game.database import initialize_static_data
from utils.loader import choose_hero, choose_equipment

def main():
    initialize_static_data()

    while True:
        print("\n=== Path of the Loner ===")
        mode = main_menu()
        if mode == "PvE":
            hero = choose_hero()
            choose_equipment(hero)
            pve_mode(hero)
        elif mode == "PvP":
            pvp_mode()
        
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
