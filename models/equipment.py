from dataclasses import dataclass

@dataclass
class Weapon:
    name: str
    power: int

@dataclass
class Armor:
    name: str
    defense: int
