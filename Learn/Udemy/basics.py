""" python 101 """

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

# list comprehension/ slicing
list3 = list2[1:]   # slice from 2nd element on
print(list3)

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

