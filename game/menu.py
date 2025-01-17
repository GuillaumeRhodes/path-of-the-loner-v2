def main_menu():
    print("=== Menu Principal ===")
    print("1. Joueur contre Environnement (JcE)")
    print("2. Joueur contre Joueur (JcJ)")
    choice = input("Choisissez votre mode (JcJ/JcE): ")
    if choice == "JcE":
        return "JcE"
    elif choice == "JcJ":
        return "JcJ"
    else:
        print("Choix invalide, saisissez JcE ou JcJ.")
        return main_menu()
