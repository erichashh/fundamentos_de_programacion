

altura = int(input("altura de la piramide:"))

for x in range(altura):
    for y in range(x + 1):
        print("*", end="")
    print()
    