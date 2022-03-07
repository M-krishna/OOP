"""
Decorator Pattern example 2

Pizza Shop
"""


from abc import ABC, abstractmethod

# abstract Pizza class
class Pizza(ABC):
    description: str

    def getDescription(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass


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

    def cost(self) -> float:
        return 100


class PizzaMargherita(Pizza):
    def __init__(self):
        self.description = "Pizza Margherita"

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
        return self.pizza.cost() + 20


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
