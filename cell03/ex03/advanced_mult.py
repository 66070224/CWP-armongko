i = 0
while True:
    if i >= 11:
        break
    print(f"Table de {i}:", end="")
    j = 0
    while True:
        print(f" {i*j}", end="")
        j +=1
        if j >= 11:
            break
    i += 1
    print()