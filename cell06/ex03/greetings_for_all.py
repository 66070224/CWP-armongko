#!/usr/bin/env python3

def greetings(name=None):
    if name == None:
        print("Hello, noble stranger.")
        return
    if not isinstance(name, str):
        print("ERROR! It was not a name.")
        return
    print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
