"""
Intro to decorators
"""


# decorator - adding additional functionality on the runtime
# commonly used in web frameworks such as flask and django e.g. routing etc.
# @ is used to declare decorators

# returning a function from within a function
def func():
    print('upper function')

    def func2():
        print('nested function')

        def func3():
            print('nested 2 levels')
            return 72

        return func3()

    return func2()


test = func()
print(test)


def cool():
    def super_cool():
        return 'I''m so fancy'

    return super_cool


# pointer/ delegate
some_func = cool()
print(some_func)


# decorator example - long way using a wrapper function

def new_decorator(original_function):
    def wrap_func():
        print('Some extra code, before the original function')
        original_function()
        print('Some extra code, after the original function')
        return 42

    return wrap_func()


def func_needs_decorator():
    print('I need to be decorated')


decorated_func = new_decorator(func_needs_decorator)
print(decorated_func)


# short way using @ declaration

@new_decorator
def func_needs_decorator2():
    print('I want to be decorated 2')
