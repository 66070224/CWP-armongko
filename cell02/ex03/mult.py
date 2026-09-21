first = int(input("Enter the first number:\n"))
sec = int(input("Enter the second number:\n"))

res = first * sec

print(f"{first} x {sec} = {res}")

if res > 0:
    print("This number is positive.")
elif res < 0:
    print("This number is negative.")
else:
    print("This number is both positive and negative.")
