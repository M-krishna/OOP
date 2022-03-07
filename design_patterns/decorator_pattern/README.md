# Decorator Pattern

The Decorator Pattern attaches additional responsibilities to an object dynamically. Decorators provide flexible alternative to subclassing for extending functionality.

# Example

Implemented the example used in the `Head first design pattern` book.

# Pizza shop example

Lets say you are running a pizza shop and your shop provides 4 varieties of Pizza with different prices and also there are different toppings that can be added to the Pizzas. For each toppings there will be a price. So we have Pizzas with different toppings that add up to a price.

Now to create an OO design for this requirement, the straight forward approach would be to use `Inheritance`. Lets see how that solution looks like
```python
class Pizza:
    description: str

    def cost(self):
        pass


class Topping(Pizza):
    pass


class CheesPizza(Pizza):
    def __init__(self):
        self.description = "Cheese pizza"

    def cost(self) -> float:
        return 100


class CheesePizzaWithToppings(Pizza, Topping):
    def __init__(self):
        self.description = "Chees pizza with olive and corn"

    def cost(self) -> float:
        return 200
```

As you can see from the above example we have to create different concrete implementations of the Pizza class for new types of pizzas. As Pizza shop grows big you may want to introduce new types of Pizza and new types of Toppings. Adding those would mean creating new classes and so it may lead to `class explosion`. So we can clearly see that `Inheritance` is not the best option to implement this Pizza shop. SO, what can we do?

### Introducing the Decorator pattern
So, to redefine our problem we have a Pizza shop that contains varieties of Pizzas and Toppings with different price points. Both Pizza and Toppings will have separate prices. We need a way combine them together and present it so that its easy for the customer to get the final product.
```python
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
        self.pizza = Pizza

    def getDescription(self) -> str:
        return f"{self.pizza.getDescription()}, olive topping"

    def cost(self) -> float:
        return self.pizza.cost() + 20


class CornTopping(Toppings):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def getDescription(self) -> str:
        return f"{self.pizza.getDescription()}, corn topping"

    def cost(self) -> float:
        return self.pizza.cost() + 10
```

From the above code example we can see that we have two `abstract` classes. One for `Pizza` and one for `Toppings`. The Pizza abstract class has `description` instance variable, `getDescription` implementation and an abstract `cost` method. Each `concrete implementation` of the Pizza class have to set the `description` and implement the `cost` method. Likewise the Toppings is an abstract class and also it inherits the Pizza class. The Toppings abstract class has a `pizza` instance variable of type `Pizza`. This is to hold the instance of the object that we want to decorate with, in this case its `Pizza`.
The concrete implementations of the `Toppings` class takes in the `Pizza` instance, implement the `getDescription` and `cost` method. 

Okay, now we have everything in place lets decorate our pizzas with toppings.
```python
cheese_pizza = CheesePizza()
print(cheese_pizza.getDescription())  # prints out the description of the CheesePizza
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
```

Looking at the above piece of code we can clearly see how easy it is to add toppings to the Pizza without modifying the existing Pizza code. We are wrapping the `Pizza` instance with the `Toppings` instance. Since `Toppings` inherits from `Pizza` we have access to the `cost` and `description` that we can use to update the `Pizza`.

This code example can be found in `decorator_pattern_example_2.py`
