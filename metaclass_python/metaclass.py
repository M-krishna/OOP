"""
Metaclass in python
"""

# In python 3 every classes are new style class


class Foo:
    pass


f = Foo()
print(f.__class__)  # __main.__.Foo
print(type(f))  # __main__.Foo

print(f.__class__ is type(f))  # True

# In python, everything is an object. Classes are objects as well. So class must have a type. What is the type of a class?
class Bar:
    pass


b = Bar()
print("instance", type(b))  # __main__.Bar
print("class", type(Bar))  # class `type`


# The type of built in classes are also `type`
for t in int, str, list, tuple, dict, float:
    print(type(t))

# So what really is the type of type?
print("type of `type` is: ", type(type))  # also `type`

# type is a metaclass, of which classes are instances. Just as an ordinary object is an instance of a class, any new-style class in Python and thus any class in Python 3, is an instance of the `type` metaclass.
# So if we take the example of Bar,
# b is an instance of Bar
# Bar is an instance of the `type` metaclass
# type is also an instance of the `type` metaclass. So it is an instance of itself.

# We can use type to create classes Dynamically
# The built in type function, when passed one argument, returns the type of an object.
# We can also call type() with 3 arguments.
# type(<name>, <bases>, <dct>)
# name - the name of class you want to create
# bases - If the class we are creating inherits any classes we need to provide it as the second argument
# dct(dict) - specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the class.

# Now lets create a class Dynamically
# Example One(create a normal class, without inheritance and class body)
FooOne = type("FooOne", (), {})
foo_one = FooOne()
print(type(foo_one))  # __main__.FooOne
print(type(FooOne))  # class type

# Example Two(create a class, that inherits from one base class)
BarOne = type("BarOne", (FooOne,), {})  # We are inheriting from FooOne
bar_one = BarOne()
print(type(bar_one))
print(type(BarOne))
print(BarOne.__bases__)  # prints the base classes of BarOne

# Example Three(create a class, that dont have any base classes, and have some attributes)
BarTwo = type("BarTwo", (), {"attr_x": 10, "attr_y": 20})
bar_two = BarTwo()
print(bar_two.attr_x)  # prints 10
print(bar_two.attr_y)  # prints 20

# we can also have functions
BarThree = type("BarThree", (), {"attr_x": 10, "attr_x_val": lambda x: x.attr_x})
bar_three = BarThree()
print(bar_three.attr_x)
print(bar_three.attr_x_val())

# Lets create a metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x


class UseMetaClass(metaclass=Meta):
    pass


class InheritFromMetaClass(UseMetaClass):
    pass


mtc = UseMetaClass()
print(mtc.attr)  # prints 100
print(UseMetaClass.attr)  # prints 100
print(UseMetaClass.__bases__)

print(InheritFromMetaClass.attr)  # prints 100
print(InheritFromMetaClass.__bases__)  # prints UseMetaClass
