# '/usr/share/dict/words'
# The above path is the dictionary of words that your computer uses


def get_words():
    """Function that reads all the words your machine is aware of and writes
    any word more than 3 characters to a new file
    """
    pass


def get_non_exists():
    """Function that demonstrates the usefulness of try/except/finally
    and exception handling in Python
    """
    try:
        with open('./eggs/bacon.ham') as f:
            print(f.read())
    except (FileNotFoundError, TypeError) as e:
        raise e
        # print(e)
        # raise FileNotFoundError('Not cool')
    finally:
        print('I ran last regardless of success or failure')


def get_binary():
    """Function that reads and exposes binary data from file.
    Useful for showing the different modes of opening a file for read/write & encoding
    """
    pass


if __name__ == '__main__':
    get_words()
    get_non_exists()
    get_binary()
