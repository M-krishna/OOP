"""
Encapsulation example
"""

class ColaMachine(object):
    
    __COLA_LIST = [] # using list data structure

    def __init__(self, **kwargs):
        self.__COLA_LIST = self.__seed_initial_data()

    def __seed_initial_data(self):
        return [
                {
                    'id': 1,
                    'name': 'a',
                    'quantity': 10
                },
                {
                    'id': 2,
                    'name': 'b',
                    'quantity': 10,
                },
                {
                    'id': 3,
                    'name': 'c',
                    'quantity': 10,
                },
                {
                    'id': 4,
                    'name': 'd',
                    'quantity': 10
                }
            ]

    def available_colas(self) -> None:
        for cola in self.__COLA_LIST:
            print(cola['name'], cola['quantity'])

    def __is_empty(self, cola_id) -> bool:
        for cola in self.__COLA_LIST:
            if cola['id'] == cola_id:
                return cola['quantity'] == 0

    def pick_cola(self, id) -> None:
        for cola in self.__COLA_LIST:
            if cola['id'] == id:
                if not self.__is_empty(cola['id']):
                    print('Here you go ',cola['name'])
                    self.__update_cola_list(id)
                else:
                   print('The cola you choose is not available')


    def __update_cola_list(self, id) -> None:
        for cola in self.__COLA_LIST:
            if cola['id'] == id:
                cola.update({'quantity': cola['quantity'] - 1})

obj = ColaMachine()
obj.pick_cola(3)
obj.available_colas()
