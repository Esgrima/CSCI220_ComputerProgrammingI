def add():
    print("Multiply & Add!")
    num = eval(input("Provide a whole number: "))

    count = 0
    for i in range(1, num):
        count = count + (i * (i + 1))
    print(count)


add()
