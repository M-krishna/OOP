# Observer pattern

The Observer pattern defines a one-to-many relationship between objects so that when one object changes state, all of its dependents are notified and updated automatically.

## Example 1

In this `The Subject` pushes the data to all the observers. There are some limitations to it. 

* Every Observer is different.
* Not every Observer needs all the data from the Subject.
* In future if we add any new data to the interface we have to update every implementations of it.

To overcome this limitations we can make the Observers `pull` the data from the Subject. Refer `Example 2` for that.

## Example 2

In this `The Subject` updates `The Observer` that the data is changed by calling the `update` method without passing any data to the method. And the Subject introduces getter methods for the respective data. On `The Observer` side
we use the newly created `getter` methods on the `Subject` to `pull` the updated data. This allows for loosely coupled design. The Observer can only pull the data it needs, nothing more nothing less.
