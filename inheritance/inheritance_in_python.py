"""
Inheritance in python

Simple example:

class ParentClass:
    body_of_parent_class

class ChildClass(ParentClass):
    body_of_child_class
"""

# Example one
class Car:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def description(self):
        print(f"The name of car is {self.name} and color is {self.color}")


class BMW(Car):
    pass


class Audi(Car):
    def audi_description(self):
        print("This is the description method of Audi class")


car = Car("BMW", "black", "x1")
car.description()

bmw = BMW("BMW", "red", "A1")
bmw.description()

audi = Audi("Audi", "white", "GQ")
audi.description()
audi.audi_description()

print(BMW.__base__, Audi.__base__, Car.__base__)  # return a single class
print(
    BMW.__bases__, Audi.__bases__, Car.__bases__
)  # returns a tuple of base classes that a child class inherits


# Single inheritance
class SIParentClass:
    def x1(self):
        print("Function of parent class")


class SIChildClass(SIParentClass):
    def x2(self):
        print("Function of child class")


obj1 = SIChildClass()
obj1.x1()  # calls the parent class function via child object
obj1.x2()

# Multiple inheritance
class MIParentClass1:
    def x1(self):
        print("Function of parent_class_1")


class MIParentClass2:
    def x2(self):
        print("Function of parent_class_2")


class MIParentClass3:
    def x3(self):
        print("Function of parent_class_3")


class MIChildClass(MIParentClass1, MIParentClass2, MIParentClass3):
    def x4(self):
        print("Function of child class")


child_obj = MIChildClass()
child_obj.x1()
child_obj.x2()
child_obj.x3()
child_obj.x4()

# Multiple inheritance with different example
# A child class inherits multiple parent classes with same function
class MINewParentClass1:
    def x1(self):
        print("Function of parent_class_1")


class MINewParentClass2:
    def x1(self):
        print("Function of parent_class_2")


class MINewChildClass(MINewParentClass1, MINewParentClass2):
    def x2(self):
        print("Function of new_child_class")


new_child_obj = MINewChildClass()
new_child_obj.x1()  # prints Function of parent_class_1
new_child_obj.x2()
print(
    MINewChildClass.__mro__
)  # reason why calling x1() prints function from parent_class_1. MRO(Method resolution order)
# In multiple inheritance, the child class first searches the method in its own class. If not found, then it searches in the parent classes depth_first and left-right order.

# complicated example to test __mro__
class ExParent1:
    pass


class ExParent2:
    pass


class ExParent3:
    pass


class ExChild1(ExParent1, ExParent2):
    pass


class ExChild2(ExParent2, ExParent3):
    pass


class ExChild3(ExChild1, ExChild2, ExParent3):
    pass


print(ExChild3.__mro__)

# Multi-level inheritance
class MLIParentClass:
    def x1(self):
        print("Function of parent class")


class MLIChildClass1(MLIParentClass):
    def x2(self):
        print("Function of child class 1")


class MLIChildClass2(MLIChildClass1):
    def x3(self):
        print("Function of child class 2")


child_1 = MLIChildClass1()
child_1.x1()
child_1.x2()

child_2 = MLIChildClass2()
child_2.x1()
child_2.x2()
child_2.x3()

# Hierarchical inheritance
class HIParentClass:
    def x1(self):
        print("Function of parent class")


class HIChildClass1(HIParentClass):
    def x2(self):
        print("Function of child class 1")


class HIChildClass2(HIParentClass):
    def x3(self):
        print("Function of child class 2")


class HIChildClass3(HIParentClass):
    def x4(self):
        print("Function of child class 3")


obj_1 = HIChildClass1()
obj_1.x1()
obj_1.x2()

obj_2 = HIChildClass2()
obj_2.x1()
obj_2.x3()

obj_3 = HIChildClass3()
obj_3.x1()
obj_3.x4()

# Hybrid inheritance
class HYIParentClass:
    def x1(self):
        print("Function of parent class")


class HYIChildClass1(HYIParentClass):  # Hierarchical inheritance
    def x2(self):
        print("Function of child class 1")


class HYIChildClass2(HYIParentClass):  # Hierarchical inheritance
    def x3(self):
        print("Function of child class 2")


class HYIChildClass3(HYIChildClass1, HYIChildClass2):  # Multiple inheritance
    def x4(self):
        print("Function of child class 3")


child_3 = HYIChildClass3()  # Together child class 3 derive Hybrid inheritance
child_3.x1()
child_3.x2()
child_3.x3()
child_3.x4()
print(HYIChildClass3.__mro__)

# Method overriding
class MOParentClass:
    def x1(self):
        print("Function of parent class")


class MOChildClass(MOParentClass):
    def x1(self):
        print("Function of child class overriding parent class")


method_override_obj = MOChildClass()
method_override_obj.x1()

method_override_parent_obj = MOParentClass()
method_override_parent_obj.x1()

# The super() function
class SuperParentClass:
    def x1(self):
        print("Function of parent class for super() example")


class SuperChildClass(SuperParentClass):
    def x1(self):
        super().x1()
        print("Function of child class for super() example")


super_child_obj = SuperChildClass()
super_child_obj.x1()


class SuperParentClass1:
    def x1(self):
        print("Function of parent class for super() example")


class SuperChildClass1(SuperParentClass1):
    def x1(self):
        super(SuperChildClass1, self).x1()
        print("Function of child class for super() example")


super_child_obj1 = SuperChildClass1()
super_child_obj1.x1()

# super() example using init method
class SuperInitParentClass:
    def __init__(self, name):
        print(name, "is derived from another class")


class SuperInitChildClass(SuperInitParentClass):
    def __init__(self, name):
        print(name, "is a sub-class")
        super().__init__(name)


siobj = SuperInitChildClass("Child")

# second use case of super() example
class First:
    def __init__(self):
        print("first")
        super().__init__()


class Second:
    def __init__(self):
        print("second")
        super().__init__()


class Third(Second, First):
    def __init__(self):
        print("Third")
        super().__init__()


obj_3 = Third()
print(First.__mro__)
print(Second.__mro__)
print(Third.__mro__)
