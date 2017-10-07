base = eval(input("Provide a base: "))
power = eval(input("Provide a power: "))
result = 1

for i in range(power):
    result = result * base
print(result)
