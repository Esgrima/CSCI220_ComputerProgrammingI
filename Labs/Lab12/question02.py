def demonstratesSets():
    setA = {1, 2, 3, 5, 7, 9}
    setB = {2, 3, 4, 6, 8, 9, 10}

    setUnion = setA.union(setB)
    print(setUnion)

    setInter = setA.intersection(setB)
    print(setInter)

    # is setA a subset of setB, Test whether every element in the set is in other.
    print(setA.issubset(setB))

    # is setA a superset of setB, Test whether every element in other is in the set.
    print(setA.issuperset(setB))

    # returns whats in the setA and not in setB
    print(setA.difference(setB))

    # returns whats in setB and not in setA
    print(setB.difference(setA))


demonstratesSets()


listUno = [True, 22, "Deadpool", "Chimichangas", False, 8.33]
listDos = ["Pineapple surprise", False, 5, 2.714, True, "Maximum Effort"]

deadpoolsDictionary = {}

for idx, key in enumerate(listUno):
    deadpoolsDictionary[key] = listDos[idx]

for keyValue in deadpoolsDictionary:
    print("{0}: {1}".format(keyValue, deadpoolsDictionary[keyValue]))
