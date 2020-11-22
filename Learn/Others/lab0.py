#!/usr/bin/python3

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    if(n2 ==  0):
        return "error, zero is invalid"
    else:
        return n1 / n2


print(add(11,20292))
print(sub(22,878))
print(mul(11,22))
print(div(1,0))


