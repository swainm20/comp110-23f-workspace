"""Demonstrates functions"""
from random import randint
"""function_name(<argument list>)
def function_name(<parameter list>) -> <return type>:
    --> above is a docstring describing function <what your function does>"""
y: str = print("Hello!")
print(y)

round(10.25)
print(round(10.25))
x: int = round(10.25)
print(x)

z: int = randint(1,7)

"""Example functions to learn definition and calling syntax"""
def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out two numbers"""
    if number1 >= number2:
        return number1
    else: #number < number2
        return number2

max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
print(max_number)

    