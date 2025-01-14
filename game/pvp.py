from utils.loader import choose_hero, choose_equipment, generate_random_hero
from game.combat import combatPvp

def pvp_mode():
    print("\n=== PvP Mode ===")
    
    print("Player 1, choose your hero and equipment.")
    player1 = choose_hero()
    choose_equipment(player1)

    player2 = generate_random_hero()
    print(f"Player 2 chose {player2.name}!")
    print(f"Player 2 is equipped with {player2.weapon.name} and {player2.armor.name}.")
    
    input("\nPress Enter to start the combat...")

    combatPvp(player1, player2)

