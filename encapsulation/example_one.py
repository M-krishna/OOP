"""
Encapsulation example
"""

class Car:
    def __init__(self, color='white'):
        self.__color = color

    def get_color(self):
        return self.__color

bmw = Car(color='Black')
print(bmw.get_color())
print(Car().__color)
