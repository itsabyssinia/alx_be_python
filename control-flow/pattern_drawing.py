row = int(input("Enter the size of the pattern: "))
i = row
while i > 0:
    for x in range(1, row + 1):
        print("*", end="")
    print()
    i -=1
