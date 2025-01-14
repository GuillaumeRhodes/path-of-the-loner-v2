from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self._hp = hp
        self.attack = attack
        self.defense = defense

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)

    @abstractmethod
    def attack_target(self, target):
        pass

    def __str__(self):
        return f"{self.name} - HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}"

class Character(Entity):
    def attack_target(self, target):
        damage = max(0, self.attack - target.defense)
        target.hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

class Archer(Character):
    def attack_target(self, target):
        print(f"{self.name} (Archer) attacks first!")
        super().attack_target(target)

class Warrior(Character):
    def attack_target(self, target):
        print(f"{self.name} (Warrior) attacks twice!")
        super().attack_target(target)
        super().attack_target(target)
