# Author: Philipp Kittler
# Date: 2024-10-26
# License: free usage for private, educational and commercial purposes, referencing appreciated

# very efficient method
def iseven_modulo(number):
    return number % 2 == 0

# very efficient method
def iseven_binary(number):
    return (number & 1) == 0

def iseven_intdev(number):
    return number / 2 == number // 2

def iseven_count(number):
    while number > 1:
        number -= 2
    return number == 0

def iseven_string(number):
    return str(number)[-1] in "02468"

def iseven_round(number):
    return round(number / 2) == number // 2

def iseven_addition(number):
    return (number + number) % 4 == 0

def iseven_recursive(number):
    if number == 0:
        return True
    elif number == 1:
        return False
    else:
        return iseven_recursive(number - 2)

def iseven_lookup(number):
    lookup = [True, False, True, False, True, False, True, False, True, False]
    return lookup[number % 10]

def iseven_isint(number):
    return (number * 0.5).is_integer()
