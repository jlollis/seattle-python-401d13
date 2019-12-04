def read_file(path):

    try:
        with open(path) as f:
            print(f.read())
    except FileNotFoundError as e:
        print('bunk')
        print(str(e))
    else:
        print('woohoo')
    finally:
        print('I always get the last word')

def write_file(path, contents):
    with open(path, 'w') as f:
        f.write(contents)

def append_file(path, contents):
    with open(path, 'a') as f:
        f.write(contents)

def read_binary_file(path):
    with open(path, 'rb') as f:
        print(f.read())

# write_file('eggs.txt','sunny side up')
# append_file('eggs.txt','over medium')
# write_file('eggs.txt','allergic')

# read_file('eggs.txt')


def add_nums(a, b):
    try:
        return a + b
    except TypeError as e:
        raise Exception('ouch')

add_nums(None, None)

