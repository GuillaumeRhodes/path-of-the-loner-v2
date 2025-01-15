from game.exploration import explore_zone

def pve_mode(hero):
    print("\n=== Mode JcE ===")
    for zone in ["normal", "elite", "boss"]:
        explore_zone(hero, zone)
        if hero.hp <= 0:
            print("Vous êtes mort!")
            return
    print("Félicitations, vous avez terminé toutes les zones!")
