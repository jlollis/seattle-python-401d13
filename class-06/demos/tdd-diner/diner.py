class Diner:
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func


    def dine(self):
        self._print('Welcome to TDD Diner')
        self._print('Home of the hottest cup of joe')
        main_dish = self._input('Enter main dish: ')
        side_dish = self._input('Enter side dish: ')
        beverage = self._input('Enter beverage: ')

        self._print(f'One order of {main_dish} with {side_dish} and {beverage} coming up!')



if __name__ == "__main__":

    def angry_print(msg):
        print('How dare you??? ' + msg)

    diner = Diner(angry_print)
    diner.dine()
