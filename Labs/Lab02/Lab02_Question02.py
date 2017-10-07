start = eval(input("What is the starting number?: "))
end = eval(input("What is the ending number?: "))

square = 0
for i in range(start, end + 1):
    square = square + i ** 2
print(square)
