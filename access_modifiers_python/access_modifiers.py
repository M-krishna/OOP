"""
Access modifiers in python
"""

# By default everything is public
class Example:
    
    class_variable_one = 1
    class_variable_two = 2
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


# Public access modifier Example
print("Public access modifiers example")
print()
public_access_modifier = Example(name='neo', age=21)
print('Name: ', public_access_modifier.name)
print('Age: ', public_access_modifier.age)
print('Name from function: ', public_access_modifier.getName())
print('Age from function: ', public_access_modifier.getAge())
print("end public access modifiers")
print()

# Private access modifier
# use __ before variable and function names to make it private to a class
# private variables, methods/functions are accessed within that class only
class PrivateAccessModifierExample:
    __class_variable_one = 1
    __class_variable_two = 2

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __getName(self):
        return self.__name

    def __getAge(self):
        return self.__age

    def accessPrivateGetName(self):
        return self.__getName()

    def accessPrivateGetAge(self):
        return self.__getAge()

    def accessPrivateClassVariable(self):
        return self.__class_variable_one


# private access modifier example
# If we try to access variables/functions that are prefixed with double underscore, we get an error
private_access_modifier = PrivateAccessModifierExample('krishna', 21)
print("Private access modifiers example")
print()
print(private_access_modifier.accessPrivateGetName())
print(private_access_modifier.accessPrivateGetAge())
print(private_access_modifier.accessPrivateClassVariable())
print("end private access modifier")
print()


# Protected access modifier
# The members that are declared protected are only accessible to a class derived from it
class ProtectedAccessModifierExample:
    _class_variable_one = 1
    _class_variable_two = 2
    __private_class_variable = 'private_class_variable'

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _getName(self):
        return self._name

    def _getAge(self):
        return self._age


class DerivedFromProtected(ProtectedAccessModifierExample):

    def __init__(self, name, age):
        super().__init__(name, age)

    def accessGetName(self):
        return self._name

    def accessGetAge(self):
        return self._age

    def accessClassVariableOne(self):
        return self._class_variable_one

    def accessPrivateClassVariable(self):
        return self.__private_class_variable


# Protected access modifier examples
protected_access_modifiers = DerivedFromProtected('Neo', 22)
print(protected_access_modifiers._class_variable_one)
print(protected_access_modifiers._name)
print(protected_access_modifiers._age)
print(protected_access_modifiers.accessPrivateClassVariable()) # throws error since its not possible to access private members of a super class in derived class
