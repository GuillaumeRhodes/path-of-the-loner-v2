import random

class Character:
    def __init__(self, name, hp, base_attack, base_defense, role=None):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.weapon = None
        self.armor = None

    @property
    def attack(self):
        # attaque de base + bonus d'arme
        return self.base_attack + (self.weapon.power if self.weapon else 0)

    @property
    def defense(self):
        # défense de base + bonus d'armure
        return self.base_defense + (self.armor.defense if self.armor else 0)

    def attack_target(self, target, role=None):
        """Effectue une attaque contre une cible."""
        damage = max(0, self.attack - target.defense)
        target.hp -= damage
        if role:
            print(f"{role} ({self.name}) attacks {target.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {target.name} for {damage} damage!")

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor

        
        

class Archer(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.dodge_rate = 0.25

    def attack_target(self, target):
        print(f"{self.name} attacks first!")
        super().attack_target(target)

    def dodge(self):
        return random.random() < self.dodge_rate


class Warrior(Character):
    def attack_target(self, target):
        print(f"{self.name} (Warrior) attacks twice!")
        super().attack_target(target)
        if target.hp > 0:
            super().attack_target(target)


class Mage(Character):
    DEFAULT_MANA = 50
    
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.mana = Mage.DEFAULT_MANA

    def cast_spell(self, target, spell_cost, spell_damage):
        if self.mana >= spell_cost:
            self.mana -= spell_cost
            damage = max(0, spell_damage - target.defense)
            target.hp -= damage
            print(f"{self.name} (Mage) casts a spell on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} doesn't have enough mana to cast the spell!")

    def attack_target(self, target, role=None):
        choice = input(f"{role} ({self.name}), do you want to (A)ttack or (C)ast a spell? ").lower()
        if choice == "c":
            self.cast_spell(target, spell_cost=10, spell_damage=30)
        else:
            super().attack_target(target)


