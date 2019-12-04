menu_template = '{} and {} with a side of {} please'

foods = ['ham', 'eggs', 'bacon']

# format expects multiple arguments vs. a list
# so using the "splat" operator aka *
# will "unpack" the list into individual arguments
formatted = menu_template.format(*foods)

print(formatted)
