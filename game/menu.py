def main_menu():
    print("=== Main Menu ===")
    print("1. Player vs Environment (PvE)")
    print("2. Player vs Player (PvP)")
    choice = input("Choose your mode (PvP/PvE): ")
    if choice == "PvE":
        return "PvE"
    elif choice == "PvP":
        return "PvP"
    else:
        print("Invalid choice, please try again.")
        return main_menu()
