import datetime


name = input("What is your name?: ")
age = input("How old are you?: ")
diff = 100 - int(age)
now = datetime.datetime.now()
century_club = now.year + diff

print(name + ", I am pleased to tell you that you will turn 100 in " + str(century_club) + ".")
