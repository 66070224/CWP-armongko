import sys

if len(sys.argv) == 3:
    amount = sys.argv[2].count(sys.argv[1])
    if amount == 0:
        print("none")
    else:
        print(amount)
else:
    print("none")
