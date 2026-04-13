# syntax: map(function, arguments)
# similar to 'for' loop 

list_A = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x * x, list_A))
print(squared_numbers)  
