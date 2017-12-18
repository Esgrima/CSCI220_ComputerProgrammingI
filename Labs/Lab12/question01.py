


class Student:
    def __init__(self, _name: str, _age: int, _major: str, _numOfHours: int):
        self.name = _name
        self.age = _age
        self.major = _major
        self.numOfHours = _numOfHours

    def __eq__(self, other):
        if (self.name == other.name) or (self.age == other.age and self.numOfHours == other.numOfHours) or \
           (self.numOfHours == other.numOfHours and self.major == other.major) or (self.age == other.age and
            self.major == other.major):
            return True
        else:
            return False

    def __len__(self):
        return self.numOfHours

    def __gt__(self, other):
        if self.numOfHours > other.numOfHours:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.numOfHours < other.numOfHours:
            return True
        else:
            return False

    def __add__(self, other):
        print("Can't add two students")
        return 0


# Testing
rex = Student("Rex", 28, "CS", 24)
rexClone = Student("Rex", 28, "CS", 24)

kobe = Student("Kobe", 37, "SM", 176)

print(len(rex))
print(rex > kobe)
print(rex < kobe)

print(kobe > rex)
print(kobe < rex)

print(rex == rexClone)

print(rex + kobe)





