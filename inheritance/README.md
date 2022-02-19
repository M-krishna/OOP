### Inheritance example

Inheritance is the procedure in which one class inherits the attributes and methods of another class. The class whose properties and methods are inherited is known as Parent class. And the class that inherits the properties from the parent class is known as Child class. 
Along with the inherited properties and methods, a Child class can have its own properties and methods.

### Inheritance syntax example in python
```python
class ParentClass:
    body_of_parent_class

class ChildClass(ParentClass):
    body_of_child_class
```

## Example one from code

In example one, we have a `Car` class that contains 3 instance variables and 1 instance method. And we have two more classes `BMW` and `Audi` which inherits from the parent class `Car`. 
We have not provided any additional properties or attributes to the `BMW` class. Whereas there is one additional method in `Audi` class. Notice we can able to access the instance method `description` of the `Parent` class from the `Child` object. This is known as Inheritance.

We can check the `base class` of a class by using `__bases__` property of the `Class`. So if we check the bases of BWM we get Car as our base class and similarly for Audi.

# Types of inheritance(Python)

* Single inheritance
* Multiple inheritance
* Multi-level inheritance
* Hierarchical inheritance
* Hybrid inheritance

### Single inheritance

This is a form of inheritance in which a class inherits only one Parent class.

### Multiple inheritance

An inheritance becomes multiple inheritances when a class inherits more the one parent class. The child class after inheriting all the properties from various parent classes has access to all of their objects.

### Multi-level inheritance

For example, a class_1 is inherited by a class_2 and class_2 is inherited by class_3 and this process goes on.

### Hierarchical inheritance

In this, various child classes inherit a single parent class.

### Hybrid inheritance

when there is a combination of more than one form of inheritance, it is known as hybrid inheritance.
