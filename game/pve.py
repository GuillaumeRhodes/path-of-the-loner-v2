from game.exploration import explore_zone

def pve_mode(hero):
    print("\n=== PvE Mode ===")
    for zone in ["normal", "elite", "boss"]:
        explore_zone(hero, zone)
        if hero.hp <= 0:
            print("Game Over!")
            return
    print("Congratulations, you cleared all zones!")
