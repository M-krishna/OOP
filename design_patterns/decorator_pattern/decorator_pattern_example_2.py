"""
Decorator Pattern example 2

Pizza Shop
"""


from abc import ABC, abstractmethod
from enum import Enum


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


# abstract Pizza class
class Pizza(ABC):
    description: str
    size: Size

    def getDescription(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass

    def setSize(self, size: Size) -> None:
        self.size = size

    @property
    def getSize(self) -> Size:
        return self.size


# abstract Toppings class
class Toppings(Pizza, ABC):
    pizza: Pizza

    @abstractmethod
    def getDescription(self) -> str:
        pass


# concrete implementation of Pizza
class CheesePizza(Pizza):
    def __init__(self):
        self.description = "Cheese pizza"
        self.size = Size.SMALL

    def cost(self) -> float:
        return 100


class PizzaMargherita(Pizza):
    def __init__(self):
        self.description = "Pizza Margherita"
        self.size = Size.MEDIUM

    def cost(self) -> float:
        return 200


# concrete implementaion of Toppings
class OliveTopping(Toppings):
    def __init__(self, pizza: Pizza):
        self.description = "olive"
        self.pizza = pizza

    def getDescription(self) -> str:
        return f"{self.pizza.getDescription()}, olive topping"

    def cost(self) -> float:
        if self.pizza.getSize == Size.SMALL:
            return self.pizza.cost() + 10
        elif self.pizza.getSize == Size.MEDIUM:
            return self.pizza.cost() + 20
        elif self.pizza.getSize == Size.LARGE:
            return self.pizza.cost() + 30
        else:
            return self.pizza.cost()


class CornTopping(Toppings):
    def __init__(self, pizza: Pizza):
        self.description = "corn"
        self.pizza = pizza

    def getDescription(self) -> str:
        return f"{self.pizza.getDescription()}, corn topping"

    def cost(self) -> float:
        return self.pizza.cost() + 10


if __name__ == "__main__":

    cheese_pizza = CheesePizza()
    print(
        cheese_pizza.getDescription()
    )  # prints out the description of the CheesePizza
    print(cheese_pizza.cost())  # prints the cost of the CheesePizza

    # add toppings
    cheese_pizza_with_olive_toppings = OliveTopping(cheese_pizza)
    print(cheese_pizza_with_olive_toppings.getDescription())  # new description
    print(cheese_pizza_with_olive_toppings.cost())  # new updated cost

    # add toppings on top of toppings
    cheese_pizza_with_olive_and_corn_toppings = CornTopping(
        cheese_pizza_with_olive_toppings
    )
    print(cheese_pizza_with_olive_and_corn_toppings.getDescription())  # new description
    print(cheese_pizza_with_olive_and_corn_toppings.cost())  # new updated cost
