"""
Decorator Pattern
"""

from abc import ABC, abstractmethod

class Beverage(ABC):

    description: str = "Unknown description"

    def getDescription(self) -> str: 
        return self.description

    @abstractmethod
    def cost(self) -> float: pass


class CondimentDecorator(Beverage, ABC):

    beverage: Beverage
    
    @abstractmethod
    def getDescription(self) -> str: pass


# Concrete Implementations of the Beverage type
class HouseBlend(Beverage):

    def __init__(self):
        self.description = "HouseBlend"

    def cost(self) -> float:
        return 10.0


class DarkRoast(Beverage):

    def __init__(self):
        self.description = "DarkRoast"

    def cost(self) -> float:
        return 20.0


# Concrete Implementations of the Condiments type
class Milk(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.description = "Milk"
        self.beverage = beverage

    def getDescription(self) -> str:
        return f"{self.beverage.getDescription()}, Milk"

    def cost(self) -> float:
        return self.beverage.cost() + 1.1

class Mocha(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.description = "Mocha"
        self.beverage = beverage

    def getDescription(self) -> str:
        return f"{self.beverage.getDescription()}, Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 2.2

# Object creation phase
house_blend = HouseBlend()
print("Description", house_blend.getDescription()) # get the description of the Beverage
print("Cost", house_blend.cost())

# create a new condiment object
house_blend_with_milk_topping = Milk(house_blend) # pass the beverage you want to decorate
print(house_blend_with_milk_topping.getDescription())

house_blend_with_milk_and_mocha_toppings = Mocha(house_blend_with_milk_topping) # here we are topping the milk condiment with mocha
print(house_blend_with_milk_and_mocha_toppings.getDescription())

# print the cost of the final decorated object
print(house_blend_with_milk_and_mocha_toppings.cost()) # print out the final cost
