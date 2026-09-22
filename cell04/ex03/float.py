#!/usr/bin/env python3

def isDecimal(val: str):
    if float(val).is_integer():
        return "integer"
    return "decimal"

print(f'This number is an {isDecimal(input("Give me a number: "))}.')
