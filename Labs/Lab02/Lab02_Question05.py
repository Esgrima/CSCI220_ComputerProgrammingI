num = eval(input("How many numbers would you like to cube and then sum?: "))

count = 0

for i in range(num):
    number = eval(input("Give me a number: "))
    count = count + number ** 3
print(count)
