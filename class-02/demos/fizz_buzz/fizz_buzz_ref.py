def fizz_buzz(num):

    word = ""

    if num % 3 == 0:
        word += "Fizz"

    if num % 5 == 0:
        word += "Buzz"

    return word or num


def fizz_buzz_sequence(nums):
    output = []
    for num in nums:
        output.append(fizz_buzz(num))

    return output


def fizz_buzz_dict(nums):
    dict = {}
    for num in nums:
        dict[num] = fizz_buzz(num)
    return dict
