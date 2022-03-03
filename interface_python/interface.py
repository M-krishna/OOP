"""
Interface in python using abstract class
"""

from abc import ABC, abstractmethod

"""
Example Interface

class Interface(ABC):

    @abstractmethod
    def method_1(self):
        pass

    @abstractmethod
    def method_2(self):
        pass
"""


class Duck:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def quack(self):
        print("Duck quack quack")

    def swim(self):
        print("I can able to swim")

    def display(self):
        print(f"My name is {self.name}")

    def fly(self):
        print("I can fly")


mallard_duck = Duck("Mallard", "white")
mallard_duck.quack()
mallard_duck.display()

domestic_duck = Duck("Domestic", "black")
domestic_duck.quack()
domestic_duck.display()

rubber_duck = Duck("Rubber", "yellow")
rubber_duck.quack()
rubber_duck.display()

# In the above created objects we have overall the same behaviours. Let's segregate it based on the Duck type


class MallardDuck(Duck):
    def quack(self):
        print("Mallard duck quack quack")


class DomesticDuck(Duck):
    def quack(self):
        print("Domestic duck quack quack")


class RubberDuck(Duck):
    def quack(self):
        print("Rubber duck sqeak sqeak")


mallard_duck_1 = MallardDuck("Mallard", "white")
mallard_duck_1.quack()

domestic_duck_1 = DomesticDuck("Domestic", "black")
domestic_duck_1.quack()

rubber_duck_1 = RubberDuck("Rubber", "yellow")
rubber_duck_1.quack()

# We have overriden the quack method for each individual duck type and have their own way of quack.
# Currently we have another problem, We have fly method on the super class and it will be available for all the duck type which inherits it.
# But not every ducks can fly, for example take rubber duck it can't fly but our current implementation allows the rubber duck object to access the fly method.
# We can obviously override the fly method for the rubber duck type but its not a trivial solution.
# Lets create an Interface for fly behaviour. And the class which implements the fly behaviour can only access the fly method


class FlyBehaviour:
    @abstractmethod
    def fly(self):
        pass


class DuckOne:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def quack(self):
        print("Duck quack quack")

    def swim(self):
        print("I can able to swim")

    def display(self):
        print(f"My name is {self.name}")


class MallardDuckOne(FlyBehaviour, DuckOne):
    def fly(self):
        print("Mallard duck one fly fly fly")


class DomesticDuckOne(FlyBehaviour, DuckOne):
    def fly(self):
        print("Domestic duck one fly fly fly")


class RubberDuckOne(DuckOne):
    pass


mallard_duck_2 = MallardDuckOne("Mallard duck", "white")
mallard_duck_2.fly()

domestic_duck_2 = DomesticDuckOne("Domestic duck", "black")
domestic_duck_2.fly()

rubber_duck_2 = RubberDuckOne("Rubber duck", "yellow")
# rubber_duck_2.fly() # not possible

# We have created an interface using abstract class and it gets implemented in the MallardDuckOne and DomesticDuckOne and also we have removed the fly method from DuckOne class so it will not be available for other subclasses which did not implement the interface.
