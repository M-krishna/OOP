### Interface in python using Abstract classes

Python don't have interface keyword built in that we can use to create interfaces. Instead we can create an abstract class which contains abstract methods which will act as a blueprint for other classes which inherit/implements
the abstract class.

In the world of OOP we use Interface to make the code more scable and reusable. Lets look at a problem if we don't use interface

### Problem if we don't use interface

We have a `Duck` class which contains methods like `quack`, `swim`, `display` and `fly`. We can create as many objects/types of Ducks we want using this `Duck` class. For example
```python
class Duck:
    def quack(self):
        pass

    def swim(self):
        pass

    def display(self):
        pass

    def fly(self):
        pass
```

Let's say we are creating objects like `Mallard`, `DomesticDuck`, `CanvasBack`, `RubberDuck` and so on. Here some of the ducks fly and some don't. For example here `DomesticDuck` and `RubberDuck` don't fly and even if they don't
fly they have `fly` method available to them. We could override this method and do nothing. But as there are so many types of ducks and some fly and some don't we have to always check and override this method.
```python
class Duck:
    def quack(self):
        pass

    def swim(self):
        pass

    def display(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):
    def fly(self):
        print("I fly faster")


class DomesticDuck(Duck):
    def fly(self):
        print("I fly slower")


mallard = MallardDuck()
mallard.fly()

domestic = DomesticDuck()
domestic.fly()

rubberduck = Duck()
rubberduck.fly()  # Not possible since rubberduck can't fly

# We can override the fly method for the rubber duck by inheriting from Duck
class RubberDuck(Duck):
    def fly(self):
        pass
```

Even though we use inheritance to override the `fly` method for `RubberDuck` the `fly` method is still available for that object. That's not something we want. It would be nice if we can pull the `fly` method from the `Duck` class and have it separate. Here comes the `Interface` solution.

### Lets create an Interface

We'll create an interface that contains the `fly` method. Whenever we create a duck if that duck fly it needs to implement this `fly` method.
```python
from abc import ABC, abstractmethod


class FlyBehaviour:
    @abstractmethod
    def fly(self):
        pass


class Duck:
    def quack(self):
        pass

    def swim(self):
        pass

    def display(self):
        pass


class MallardDuck(FlyBehaviour, Duck):
    def fly(self):
        print("I fly faster")


class DomesticDuck(FlyBehaviour, Duck):
    def fly(self):
        print("I fly slower")


class RubberDuck(Duck):
    pass


rubberduck = RubberDuck()
rubberduck.fly()  # fly method will not be available since we removed it from the Duck class
```
