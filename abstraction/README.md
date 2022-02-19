# Abstraction example

Definition: Abstraction is the concept of OOP that "shows" only essential attributes and "hides" unnecessary information. The main purpose of abstraction is hiding the unnecessary details from the user.

## Cola Machine example

Lets take the same cola machine example that we used in encapsulation. The Cola machine class contains some attributes and members that are public and private. From the user stand point, the users who interact with the cola object
only care about choosing cola and getting it from the Cola machine. They don't care about how the gets picked by the machine and the internal mechanisms.

### Public methods in Cola Machine

* `available_colas`
* `pick_cola`

By only using the above two methods a user can interact with the cola object. Also they don't care about the internal things.

### Private methods in Cola Machine

* `__seed_initial_data`
* `__is_empty`
* `__update_cola_list`

The above methods are essential ones for the Cola Machine to operate properly. And the user cannot able to access them and they don't care.
