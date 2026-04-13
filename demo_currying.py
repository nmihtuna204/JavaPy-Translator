"""
We can use higher-order functions to convert a function 
that takes multiple arguments into a chain of functions 
that each take a single argument. 

More specifically, given a function f(x, y), 
we can define a function g such that g(x)(y) is equivalent to f(x, y). 
Here, g is a higher-order function that takes in a single argument x 
and returns another function that takes in a single argument y. 

This transformation is called currying.
"""

def discount(rate):
    def apply(price):        
        return price - price * rate / 100
    return apply

print(discount(10)(200))

