import random

class Character:
    def __init__(self, name, hp, base_attack, base_defense, role=None):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.weapon = None
        self.armor = None
        self.role = role
        

    @property
    def attack(self):
        # attaque de base + bonus d'arme
        return self.base_attack + (self.weapon.power if self.weapon else 0)

    @property
    def defense(self):
        # défense de base + bonus d'armure
        return self.base_defense + (self.armor.defense if self.armor else 0)

    def attack_target(self, target):
        damage = max(0, self.attack - target.defense)
        target.hp -= damage

        role_display = self.role
        print(f"{role_display} ({self.name}) attaque son adversaire et inflige {damage} dégats!")


    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor

        
        

class Archer(Character):
    def __init__(self, name, hp, attack, defense, role=None):
        super().__init__(name, hp, attack, defense)
        self.dodge_rate = 0.25
        self.role = role if role else "Unknown Role"

    def attack_target(self, target, role=None):
        print(f"{self.role} (Archer) attacks first!")
        super().attack_target(target)

    def dodge(self):
        print(f"{self.role} (Archer) dodges the attack!")
        return random.random() < self.dodge_rate


class Warrior(Character):
    def __init__(self, name, hp, attack, defense, role=None):
        super().__init__(name, hp, attack, defense)
        self.role = role if role else "Unknown Role"
        
    def attack_target(self, target):
        print(f"{self.role} (Guerrier) attaque deux fois!")
        super().attack_target(target)
        if target.hp > 0:
            super().attack_target(target)



class Mage(Character):
    DEFAULT_MANA = 50

    def __init__(self, name, hp, attack, defense, role=None):
        super().__init__(name, hp, attack, defense)
        self.mana = Mage.DEFAULT_MANA
        self.role = role if role else "Unknown Role"

    def cast_spell(self, target, spell_cost, spell_damage):
        if self.mana >= spell_cost:
            self.mana -= spell_cost
            damage = max(0, spell_damage - target.defense)
            target.hp -= damage
            print(f"{self.role} (Mage) lance un sort sur {target.name} et inflige {damage} dégâts!")
        else:
            print(f"{self.role} (Mage) n'a pas assez de mana pour lancer le sort!")

    def attack_target(self, target):
        choice = input(f"{self.role} (Mage), voulez-vous (A)ttaquer ou (L)ancer un sort? ").lower()
        if choice == "l":
            self.cast_spell(target, spell_cost=10, spell_damage=30)
        else:
            super().attack_target(target)



