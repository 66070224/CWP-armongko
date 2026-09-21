import sys

if len(sys.argv) == 2:
    num = sys.argv[1].count("z")
    if num != 0:
        print("z"*num)
    else:
        print("none")
else:
    print("none")
