#!/usr/bin/env python3

import sys

if len(sys.argv) > 0:
    for i in range(len(sys.argv)):
        if i == 0:
            print("parameters: ", len(sys.argv)-1)
            continue
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
else:
    print("none")
