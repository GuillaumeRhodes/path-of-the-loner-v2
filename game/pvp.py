from utils.loader import choose_hero, choose_equipment, generate_random_hero
from game.combat import combatPvp

def pvp_mode():
    print("\n=== Mode JcJ ===")
    
    print("Joueur 1, choisissez votre équipement.")
    player1 = choose_hero()
    choose_equipment(player1)

    player2 = generate_random_hero()
    print(f"Le Joueur 2 sélectionne un {player2.name}!")
    print(f"Le Joueur 2 s'équipe avec {player2.weapon.name} et {player2.armor.name}.")
    
    input("\nAppuyez sur Entrer pour commencer le combat...")

    combatPvp(player1, player2)

