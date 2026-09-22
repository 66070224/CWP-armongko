#!/usr/bin/env python3

import sys

def shrink(val: str):
    return val[:8]

def enlarge(val: str):
    if len(val) >= 8:
        return val
    return val+ "Z"*(8-len(val))

if len(sys.argv) > 1:
    for argv in sys.argv[1::]:
        print(shrink(enlarge(argv)))
else:
    print("none")
