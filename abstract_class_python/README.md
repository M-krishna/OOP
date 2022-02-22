### Abstract class in python

## But first what is an Abstract class?

An Abstract class is a class,  but not one you can create objects from directly. Its purpose is to define how other classes should look like (ie) what methods and properties that are expected to have.
The methods and properties are defined(but not implemented) in an abstract class are class `abstract methods` and `abstract properties`. All abstract methods and properties need to be implemented in a `Child class` in order
to be able to create objects from it.

### Python specific

We can create an abstract class by inheriting from the `ABC` class which is part of the `abc` module.
```python
from abc import	ABC, abstractmethod
```

### When should I use Abstract class?

* Avoid code duplication
* Ensure consistency in how others implement methods and properties in subclasses
* Ensure no one forgets to implement the methods and properties in subclasses
