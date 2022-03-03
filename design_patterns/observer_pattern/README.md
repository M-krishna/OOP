# Observer pattern

The Observer pattern defines a one-to-many relationship between objects so that when one object changes state, all of its dependents are notified and updated automatically.

## Example 1

In this `The Subject` pushes the data to all the observers. There are some limitations to it. 

* Every Observer is different.
* Not every Observer needs all the data from the Subject.
* In future if we add any new data to the interface we have to update every implementations of it.

To overcome this limitations we can make the Observers `pull` the data from the Subject. Refer `Example 2` for that.

## Example 2


