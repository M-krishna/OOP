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

### Method Overriding

Method overriding gives special permission of Child/SubClass to provide specific implementation to a method that is already present in Parent class.

### The super() function

The super function in python returns a `proxy object` that references the parent class using the super keyword. This `super()` keyword is basically useful in accessing the overriden methods of the parent class.

### Two main uses of super() function

1) In a class hierarchy with single inheritance, super helps to refer to the parent class without naming them explicitly, thus making the code more maintainable.
```python
class Parent:
    def x1(self):
        print("function of parent class")

class Child(Parent):
    def x1(self):
        super().x1()
	print("function of child class")

obj2 = Child()
obj2.x1() # prints function of parent class first and function of child class second
```

`super()` also accept parameters - first is the name of the Subclass and second is an object that is an instance of the subclass.
```python
class Parent:
    def x1(self):
        print("function of parent class")

class Child(Parent):
    def x1(self):
        super(Child, self).x1() # here self is the instance of the subclass
	print("function of child class")

obj2 = Child()
obj2.x1() # prints function of parent class first and function of child class second
```
2) The second use case is to support cooperative multiple inheritance in a dynamic execution environment
