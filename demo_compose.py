def compose(f, g):
    return lambda x: f(g(x))

def add1(x):
    return x + 1

def times2(x):
    return x * 2

# Compose: add1(times2(x)) = (x * 2) + 1
composed = compose(add1, times2)

print(composed(3))  # Output: 7
