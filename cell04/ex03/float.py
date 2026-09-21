def isDecimal(val: str):
    try:
        if float(val).is_integer(): 
            return "integer"
        else:
            return "decimal"
    except ValueError:
        return "integer"

print(f"This number is an {isDecimal(input("Give me a number: "))}.")