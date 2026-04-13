# Syntax: filter(function, arguments)
# similar to if condition

list_A = [1, 2, 3, 4, 5]

tmp_A = []
for a in list_A:
    if(a%2==0):
        tmp_A.append(a)

even_numbers = list(filter(lambda x: x % 2 == 0, list_A))
print(even_numbers)  
