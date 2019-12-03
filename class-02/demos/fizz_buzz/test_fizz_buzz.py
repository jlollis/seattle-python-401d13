from fizz_buzz_module import fizz_buzz_function, fizz_buzz_sequence


def test_one():
    expected = 1
    actual = fizz_buzz_function(1)
    assert actual == expected


def test_two():
    expected = 2
    actual = fizz_buzz_function(2)
    assert actual == expected


def test_three():
    expected = 'Fizz'
    actual = fizz_buzz_function(3)
    assert actual == expected


def test_four():
    expected = 4
    actual = fizz_buzz_function(4)
    assert actual == expected


def test_five():
    expected = 'Buzz'
    actual = fizz_buzz_function(5)
    assert actual == expected


def test_sixty():
    expected = 'FizzBuzz'
    actual = fizz_buzz_function(60)
    assert actual == expected


def test_fizz_buzz_list():
    expected = [1, 2, 'Fizz', 4, 'Buzz', 'FizzBuzz']
    actual = fizz_buzz_sequence([1, 2, 3, 4, 5, 60])
    assert actual == expected


def test_fizz_buzz_tuple():
    expected = [1, 2, 'Fizz', 4, 'Buzz', 'FizzBuzz']
    actual = fizz_buzz_sequence((1, 2, 3, 4, 5, 60))
    assert actual == expected

