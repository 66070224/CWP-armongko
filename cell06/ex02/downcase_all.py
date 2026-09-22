#!/usr/bin/env python3

import sys

def downcase_it(val: str):
    return val.lower()

if len(sys.argv) > 1:
    for argv in sys.argv[1::]:
        print(downcase_it(argv), end=" ")
    print()
else:
    print("none")
