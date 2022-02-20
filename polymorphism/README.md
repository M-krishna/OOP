### Polymorphism

Polymorphism means "many-shapes" or "many-forms". In programming, polymorphism means same function name(but different signatures) being used for different types. Polymorphism and Inheritance works together.
It refers to the use of a single type entity(method, operator or object) to represent different types in different scenarios.

### Examples

## Polymorphism in addition operator
```python
num1 = 1
num2 = 2
res = num1 + num2 # res = 3

str1 = "hello"
str2 = "world"
res = str1 + str2 # res = helloworld
```
Here the same `+` operator works differently in different scenarios

## Function Polymorphism
```python
len("helloworld") # returns 10
len([1, 2, 3]) # returns 3
len({"name": "neo", "age": 21}) # return 2(number of keys)
```

## Class Polymorphism
See the code example file

## Polymorphism and Inheritance
See the code example file
