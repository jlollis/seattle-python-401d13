def fizz_buzz_function(num):

    results = ''

    if num % 3 == 0:
        results += 'Fizz'

    if num % 5 == 0:
        results += 'Buzz'

    return results or num


def fizz_buzz_sequence(nums):
    return [fizz_buzz_function(num) for num in nums]

    # converted = []
    # for num in nums:
    #     val = fizz_buzz_function(num)
    #     converted.append(val)

    # return converted
