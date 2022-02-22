"""
Abstract class in python

Python by default don't have abstract keyword that can be used to make abstract class.

Instead we can import ABC(Abstract base class) from abc module/package which contains all the necessary things that we need to make a class Abstract.
"""


from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

class Pikachu(Pokemon):
    def attack(self):
        return "Thunder bolt"

class Charizard(Pokemon):
    def attack(self):
        return "Flamethrower"

# pokemon_obj = Pokemon('Hashira') # TypeError: Can't instantiate abstract class Pokemon with abstract method attack
pikachu_obj = Pikachu('Hashira')
print(pikachu_obj.attack())

charizard_obj = Charizard('Inosuke')
print(charizard_obj.attack())
