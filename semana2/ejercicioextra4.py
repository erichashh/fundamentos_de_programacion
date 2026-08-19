

altura = int(input("altura de la piramide:"))

for i in range(altura):
    for j in range(i + 1):
        print("*", end="")
    print()