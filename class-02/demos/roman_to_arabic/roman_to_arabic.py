def roman_to_arabic(roman):

  value_map = {
    'm' : 1000,
    'd' : 500,
    'c' : 100,
    'l' : 50,
    'x' : 10,
    'v' : 5,
    'i' : 1
  }

  total = 0

  end = len(roman)

  i = 0

  while i < end:

    current_char = roman[i]

    current_val = value_map[current_char]

    if i < end - 1:
      next_char = roman[i + 1]
      next_value = value_map[next_char]

      # check for subtractor
      if next_value > current_val:
        total += next_value - current_val
        i += 2 #increment twice because current value uses current and next character
        continue

    total += current_val
    i += 1

  return total
