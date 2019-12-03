from fizz_buzz import fizz_buzz, fizz_buzz_sequence, fizz_buzz_dict


def test_exists():
    assert fizz_buzz


def test_1():
    expected = 1
    actual = fizz_buzz(10)
    assert actual == expected


def test_2():
    expected = 2
    actual = fizz_buzz(2)
    assert actual == expected


def test_3():
    expected = "Fizz"
    actual = fizz_buzz(3)
    assert actual == expected


def test_5():
    expected = "Buzz"
    actual = fizz_buzz(5)
    assert actual == expected


def test_15():
    expected = "FizzBuzz"
    actual = fizz_buzz(15)
    assert actual == expected


def test_sequence():
    nums = range(1, 17)

    expected = [
        1,
        2,
        "Fizz",
        4,
        "Buzz",
        "Fizz",
        7,
        8,
        "Fizz",
        "Buzz",
        11,
        "Fizz",
        13,
        14,
        "FizzBuzz",
        16,
    ]

    actual = fizz_buzz_sequence(nums)

    assert actual == expected


def test_fizz_buzz_dict():
    nums = range(1, 17)

    expected = {
        1: 1,
        2: 2,
        3: "Fizz",
        4: 4,
        5: "Buzz",
        6: "Fizz",
        7: 7,
        8: 8,
        9: "Fizz",
        10: "Buzz",
        11: 11,
        12: "Fizz",
        13: 13,
        14: 14,
        15: "FizzBuzz",
        16: 16,
    }

    actual = fizz_buzz_dict(nums)

    assert actual == expected
