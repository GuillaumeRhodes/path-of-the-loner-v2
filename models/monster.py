from models.entity import Entity

class Monster(Entity):
    def __init__(self, name, hp, attack, defense, type_):
        super().__init__(name, hp, attack, defense)
        self.type = type_

    def attack_target(self, target):
        damage = max(0, self.attack - target.defense)
        target.hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

class NormalMonster(Monster):
    def special_ability(self):
        print(f"{self.name} has no special ability.")

class EliteMonster(Monster):
    def special_ability(self):
        print(f"{self.name} deals extra damage!")
        self.attack += 5

class BossMonster(Monster):
    def special_ability(self):
        print(f"{self.name} regenerates health!")
        self.hp += 10
