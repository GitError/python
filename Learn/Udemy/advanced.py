''' 
Python - Extra topics
''' 

from collections import Counter
from collections import defaultdict
from collections import OrderedDict

# count # of element occurrences in a collection 
l = [1,2,3,1,2,3,2,2,2,1,2,3,4,5,6,7,7,5,6,5,4,3,4,3,]
x = Counter(l)
print(x)

# using strings
s = 'How many times times each word show up'
x = s.split()
y = Counter(x)
print(y)

#   Common patterns when using Counter() object
#   ----------------------------------------------
#   Func:                         Decs:
#   sum(c.values())               -- total of all counts
#   c.clear()                     -- reset all counts
#   list(c)                       -- list of unique elements
#   set(c)                        -- convert to a set
#   dict(c)                       -- convert to a regular dictionary 
#   c.items()                     -- conevert top  a list of (elem, cnt) pairs
#   Counter(dict(list_of_pairs))  -- convert from a list (elem, cnt) pairs
#   c.most_common()[: -n-1:-1]    -- n least common elements
#   c+= Counter()                 -- remove zero and negative counts


# Default Dictionary -- defaultdict
# defaultdics is a dictionary like object which provides all methods provided by dictionary 
# but takes first argument (default_factory) as a default data type for the dictionary. 
# Using defaultdict ius faster than doing the same using dict.set_default method

# e.g. 
# d = {}
# d['one']
# results in KeyError
# d2 = defaultdict(lambda: 0)
# d2['one'] -- will return 0 instead of a KeyError

d = defaultdict(lambda: 0)
d['key2'] = 4
print(d['key1'])

# Ordered Dictionary -- OrderedDict
