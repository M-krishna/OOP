"""
Inheritance example
"""

# Example for single inheritance
class Animal:
    pass


class Lion(Animal):
    pass


# Example for Hierarchical inheritance
class Dog(Animal):
    pass


class Tiger(Animal):
    pass


class Deer(Animal):
    pass


# Example for Multi-level inheritance
class Reptile(Animal):
    pass


class Frog(Reptile):
    pass


class Turtle(Reptile):
    pass


class Bird(Animal):
    pass


class Chicken(Bird):
    pass


# Example for Multiple inheritance
class Fish(Animal):
    pass


class Aquatic(Fish):
    pass


class Terrestrial(Reptile):
    pass


class Crocodile(Aquatic, Terrestrial):
    pass


# Example for hybrid inheritance(combination of multi-level and single level inheritance)
# Animal -> Reptile -> Crocodile
#        -> Reptile -> Turtle
#        -> Reptile -> Lizard
