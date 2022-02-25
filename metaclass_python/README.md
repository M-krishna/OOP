### What is Metaclass?

To put in simple terms, Metaclasses are blueprint for classes like how classes are blueprint for objects.:

### Custom Metaclass

Lets look at an example
```python
class Foo:
	pass

f = Foo()
```

The expression `Foo()` creates a new instance of class `Foo`. When the interpreter encounters `Foo()` the following occurs:

* The `__call__()` method of `Foo's` parent class is called. Since `Foo` is the standard new style class its parent class is the `type` metaclass. So type's `__call__()` method is invoked.

* The `__call__()` method in turn invokes the following:
	* __new__()
	* __init__()

If `Foo` does not define `__new__()` and `__init__()`, default methods are inherited from `Foo`s ancestory. But if `Foo` does define these methods, they override those from the ancestory, which allows for customised behavior when instantiating `Foo`.

We can't reassign the `__new__` method of the `type` metaclass. Example:
```python
def new(cls):
	x = type.__new__(cls)
	x.attr = 10
	return x

type.__new__ = new # throws error
```

But we can inherit the `type` metaclass and define our own custom behavior of class instantiation. Example:
```python
class Meta(type):
	def __new__(cls, name, bases, dct):
		x = super().__new__(cls, name, bases, dct)
		x.attr = 10
		return x
```
Explanation for the above code:

The definition `class Meta(type):` specifies that `Meta` derives from `type`. Since type is a metaclass that makes Meta a metaclass as well. 
We have defined a custom `__new__()` method for Meta. It was not possible to do to the `type` metaclass directly. The `__new__()` method does the following

* Delegates via `super()` to the `__new__()` method of the parent class(type) to actually create a class.
* Assigns the custom attribute attr to the class, with a value of 100
* Returns the newly created class.

Now lets use this newly created metaclass.
```python
class Foo(metaclass=Meta):
	pass

print(Foo.attr) # prints 10
```
We have successfully created a metaclass and used it.
