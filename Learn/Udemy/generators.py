'''
Intro to python generators
'''

# generators allow us to generate a sequence of values over time
# the main difference in syntax is the use of yield statement 
# -- return one element at the time, no need to store entire list in memory
# e.g. range() is a generator

# in memory list example
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))

# generator - way more memory efficient
def cubes(n):
    for x in range(n):
        yield x**3

print(cubes(10))

# generator objects (return of generator function) need to be iterated over

def gen_fibon(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a,b = b, a+b

print(list(gen_fibon(10)))