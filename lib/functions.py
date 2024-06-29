#!/usr/bin/env python3

def greet_programmer(name ="programmer"):
    print(f"Hello, {name}!")
    pass

def greet(name = "Guido"):
    print(f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1 = 45, num2 = 55):
    return(num1 + num2)
    print(add)
    pass

def halve(number = 100):
    return (number/2)
    print(halve)
    pass
