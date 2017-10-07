def myFactorial():
    print("Factorial Calculator!")
    num = eval(input("Provide a whole number: "))

    fact = 1
    for i in range(num):
        fact *= (num - i)
    print(fact)


myFactorial()
