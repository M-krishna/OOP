"""
Polymorphism
"""

# Example of class Polymorphism
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Bark Bark!")

    def intro(self):
        print(f"My name is {self.name} and my age is {self.age}")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow Meow!")

    def intro(self):
        print(f"My name is {self.name} and my age is {self.age}")

dog_obj = Dog('Max', 3)
cat_obj = Cat('Kitty', 4)

for animal in (dog_obj, cat_obj):
    animal.speak()
    animal.intro()


# Example of Polymorphism and Inheritance(Method overriding)
class Shape:
    def __init__(self, name):
        self.name = name

    def fact(self):
        return "I am a 2 dimensional shape"

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__('Square')
        self.length = length

    def area(self):
        return self.length**2

    def fact(self): # overriden the fact method of parent class
        return "I am Square shape"

square_obj = Square(10)
print(square_obj.fact())
print(square_obj.area())
print(square_obj.__str__())
