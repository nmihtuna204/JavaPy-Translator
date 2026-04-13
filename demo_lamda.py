# syntax: lambda arguments:expression 
# traditional way
def sum(x, y):
    tmp = x+ y
    return tmp

# Lambda func
add_LF = lambda x, y: x + y
min_LF = lambda x, y: min(x, y)

# Function call
print(add_LF(2, 3))  
