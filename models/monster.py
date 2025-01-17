from models.entity import Entity

class Monster(Entity):
    def __init__(self, name, hp, attack, defense, type_):
        super().__init__(name, hp, attack, defense)
        self.type = type_

    def attack_target(self, target):
        damage = max(0, self.attack - target.defense)
        target.hp -= damage
        print(f"{self.name} attaque {target.name} et lui fait {damage} dégats!")

class NormalMonster(Monster):
    def special_ability(self):
        print(f"{self.name} n'a pas de coméptence spéciale.")

class EliteMonster(Monster):
    def special_ability(self):
        print(f"{self.name} fais des dégats accrus!")
        self.attack += 5

class BossMonster(Monster):
    def special_ability(self):
        print(f"{self.name} régénère ses PV!")
        self.hp += 10
