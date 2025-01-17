from game.screens.choose_armor_screen import choose_armor_screen
from utils.loader import choose_hero, generate_random_hero
from game.combat import combatPvp

def pvp_mode(screen, font):
    print("\n=== Mode JcJ ===")

    # Joueur 1 : Choix du héros et de l'équipement
    player1 = choose_hero(screen, font)
    choose_armor_screen(player1, screen, font)

    # Joueur 2 : Héros généré aléatoirement
    player2 = generate_random_hero()
    print(f"Le Joueur 2 sélectionne un {player2.name}.")
    print(f"Le Joueur 2 s'équipe avec {player2.weapon.name} et {player2.armor.name}.")

    input("\nAppuyez sur Entrer pour commencer le combat...")
    combatPvp(player1, player2)
