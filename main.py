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
        if mode == "JcE":
            hero = choose_hero()
            choose_equipment(hero)
            pve_mode(hero)
        elif mode == "JcJ":
            pvp_mode()
        
        replay = input("\nVoulez vous rejouer? (o/n): ").lower()
        if replay != "o":
            print("Merci d'avoir joué!")
            break

if __name__ == "__main__":
    main()
