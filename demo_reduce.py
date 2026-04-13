# Syntax: reduce(f, list)

from functools import reduce

# traditional approach
def sum(x,y):
    return x+y

# reduce function approach
list_A = [1, 2, 3, 4, 5]

min_element = reduce(lambda x, y: min(x,y), list_A)
print(min_element)

sum_of_numbers = reduce(lambda x, y: x + y, list_A)
print(sum_of_numbers) 
