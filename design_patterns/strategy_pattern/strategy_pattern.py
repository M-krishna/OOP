# Strategy pattern

from abc import ABC, abstractmethod


# Weapon behavior interface
class IWeaponBehavior(ABC):

    @abstractmethod
    def useWeapon(self):
        pass


# Different types of behaviors that implement IWeaponBehavior
class KnifeBehavior(IWeaponBehavior):

    def useWeapon(self):
        print("Using Knife to fight now")

class BowAndArrowBehavior(IWeaponBehavior):
    
    def useWeapon(self):
        print("Using Bow and Arrow to fight now")

class AxeBehavior(IWeaponBehavior):

    def useWeapon(self):
        print("Using Axe to fight now")

class SwordBehavior(IWeaponBehavior):

    def useWeapon(self):
        print("Using Sword to fight now")
# End of behaviors


# Character abstract class
class Character(ABC):

    # attribute
    weapon: IWeaponBehavior

    @abstractmethod
    def fight(self):
        pass

    def setWeapon(self, wb: IWeaponBehavior):
        self.weapon = wb 

# Different types of characters
class King(Character):

    def __init__(self):
        self.weapon = KnifeBehavior()

    def fight(self):
        self.weapon.useWeapon()

class Queen(Character):

    def __init__(self):
        self.weapon = BowAndArrowBehavior()

    def fight(self):
        self.weapon.useWeapon()

class Knight(Character):

    def __init__(self):
        self.weapon = SwordBehavior()

    def fight(self):
        self.weapon.useWeapon()

class Troll(Character):

    def __init__(self):
        self.weapon = AxeBehavior()

    def fight(self):
        self.weapon.useWeapon()
# End of characters

# Creating objects / Instantiating objects
king = King()
king.fight() # using the default behavior of the King
king.setWeapon(BowAndArrowBehavior()) # updating the behavior at runtime
king.fight() # invoking the updated behavior

queen = Queen()
queen.fight()
queen.setWeapon(KnifeBehavior())
queen.fight()


knight = Knight()
knight.fight()
knight.setWeapon(BowAndArrowBehavior())
knight.fight()


troll = Troll()
troll.fight()
troll.setWeapon(SwordBehavior())
troll.fight()
