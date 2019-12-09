class Diner:
    def __init__(self, print_func=print,input_func=input):
        self._print = print_func
        self._input = input_func

    def dine(self):
        self._print('Welcome to TDD Diner')
        main = self._input('Enter main dish: ')
        side_1 = self._input('Enter first side: ')
        side_2 = self._input('Enter second side: ')
        self._print(f'One order of {main} with a side of {side_1} and {side_2} coming right up!')


if __name__ == "__main__":
    diner = Diner()
    diner.dine()
