import sys

produce = {
    'apple' : 0,
    'banana' : 0,
    'cucumber' : 0
}

def exit_app():
    print('adios')
    sys.exit()

while True:
    answer = input('Pick a fruit or veggie')

    if answer == 'bail':
        exit_app()

    if answer in produce:
        produce[answer] += 1
        print(produce[answer])
    else:
        print('huh????')


print('hhooory')










