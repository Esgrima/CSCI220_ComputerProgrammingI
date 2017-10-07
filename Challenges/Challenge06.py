num = eval(input("Provide me with a number?: "))
count = 1

for i in range(num, 0, -1):
    print("  " * i + " *" * count)
    count = count + 1
