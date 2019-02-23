""" this is a docstring; python 101 """

from random import shuffle

# strings - ordered sequence of characters
my_str = 'hello'
print(my_str[2])

# booleans - true/ false;
my_bool = False
print(my_bool)

# lists - sorted, ordered sequence of objects (mutable)
list1 = []
list2 = ["one", 2, 3, 4, 5]
list2.append(6)
list2.append(7)
list2.pop(-1)   # default =-1 i.e. the last element
print(list2)

# list slicing
list3 = list2[1:]   # slice from 2nd element on
print(list3)

# list comprehension [ item_output expression for item_output in list ]
# can also add if() front of item_output
list4 = [x for x in range(100)]

# dictionaries - mutable, unordered, unsorted, key-value pairs
my_dict = {'key1': 'value1', 'key2': 'value2',
           'key3': ['one', 'two', 'three', 4, 5, 6]}
print(my_dict['key3'])

# tuples - ordered sequence of objects (immutable)
tup = (1, 2, 3, 4, 4, 4)
print(tup[3])
print(tup.count(4))

# sets - unordered collections of unique elements
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2)
print(my_set)

# file i/o
# use context manager (with syntax) when using files so that it's properly 'disposed'
with open('file.txt', 'r+') as f:
    print(f.readlines())
    f.write('\n\n...some text...')
    print(f.readlines())

# comparison and logical operators
# == != < > <= >=  --- and or not
print(not True == False or False != True)

# control statements
# range() -- range(start, stop[, steps])  -- default = range(stop, step=1)
for item in range(100):
    if(item % 12 == 0):
        print(item)
    else:
        pass

# tuple unpacking
tup_list = [(1, 2), (3, 4), (5, 6)]
for (a, b) in tup_list:
    print(a)

# apply the same syntax on dictionaries

# break -- breaks out of the current loop
# continute -- skips iteration/ go to the top of the loop
# pass -- do nothing

c = 0
while c < 5:
    print(c)
    c += 1

# enumerate(list) will create index, object in a for loop syntax
# zip is combining lists together

# inline operator
'x' in ['x', 'y', 'z']  # evaluates to true

# shuffle
print(shuffle(list(9, 81, 2, 3)))

# input() -- return value always a string

# methods - functions build into objects e.g. 
list4.append(96)

# functions - 'statics'; 
def function_name(param1, param2='default'):
    """
    docstring: explaining function
    input: desc
    output: desc
    """
    return True

# inline if -- return true if a>b else False

# *args     -- unlimited # of unnamed parameters    -- list
# **kwargs  -- unlimited # of keyword arguments     -- dictionary

# always use .lower() when comparing strings to cover all scenarios
# str.capitalize() is the same as str[0].upper()

# str.join() -- joins list with the string as a delimeter

# abs() -- absolute value of a number

# map() -- takes a function and a list and applies function on list elements
my_num = [1,2,3,4,5,6]

def square(num):
    return num**2

squares = list(map(square, my_num))

# filter() -- takes a function and a list and applies function to the list
for n in filter(square, my_num):
    print(n)

# lambdas -- same as in .net, anon in-line functions e.g. square
lambda num: num**2

# global variables -- use keyword global in front of variable name; avoid;
