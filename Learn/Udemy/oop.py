"""
Object oriented programming in python
"""

import unittest


# self. is the same as this.
# class names - use camel casing 
# methods - use lower casing and underscores
# class properties = class attributes
# constructor = __init__(self, args**) 

class Dog():
    # class object attributes/ constants
    species = 'mammal'

    def __init__(self, breed):
        self.breed = breed

    def speak(self):
        print('woof')

    def bark(self, num):
        for _ in range(num):
            print("woof ")


# inheritance
# pass base class as a parameter in derived class constructor 
# e.g. base class -- moreless an abstract class

class Animal():
    def __init__(self):
        print('animal created')

    def who_am_i(self):
        print('i am an animal')

    def eat(self):
        print('i am eating')


class MoreAbstractClass():

    def __init__(self, *args, **kwargs):
        pass

    def abstract_method(self):
        raise NotImplementedError('derived class must implement this method')


# e.g. deriver class

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('cat created')

    def speak(self):
        print('meow')


# polymorphism
# when object share the same methods
# pass an object as a parameter to the method 
# it'll be auto resolved based on its type e.g. 

def pet_speak(pet):
    print(pet.speak())


#  special methods (__ - dunder)
#  __init__(self) - constructor     __str__(self) - to string
#  __len__(self) - length           __del__(self) - delete

# when using tuples in classes unpacking can be done in __init__ or any other method

# unittest - a built-in library
# unit testing using a test class e.g. 

class TestCap(unittest.TestCase):

    def test_one(self):
        text = 'python'
        result = str.capitalize(text)
        self.assertEqual(result, 'Python')
