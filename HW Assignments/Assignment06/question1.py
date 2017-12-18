class SalesPerson:
    def __init__(self, _id: int, _personName:str):
        self.id = _id
        self.personName = _personName
        self.sales = []

    def getId(self):
        return self.id

    def getPersonName(self):
        return self.personName

    def setPersonName(self, _personName: str):
        self.personName = _personName

    def enterSale(self, _aSale: float):
        self.sales.append(_aSale)

    def totalSales(self):
        return sum(self.sales)

    def getSales(self):
        return self.sales

    def metQuota(self, _quota: float):
        if self.totalSales() >= _quota:
            return True
        else:
            return False

    def compareTo(self, _otherPerson):
        if self.totalSales() > _otherPerson.totalSales():
            return 1
        elif self.totalSales() < _otherPerson.totalSales():
            return -1
        else:
            return 0

    def __str__(self):
        return "ID: {0}\nName: {1}\nTotal Sales: ${2:0.2f}".format(self.getId(), self.getPersonName(), self.totalSales())

class SalesForce:
    def __init__(self):
        self.salesForce = []

    def addData(self, _fileName):
        # opens file for reading
        salesData = open("salesdata.txt", 'r')

        # loops through each line(employee)
        for salesPerson in salesData.readlines():
            # splits the line by space and stores it
            employee = salesPerson.split()
            # stores the employee name with a space between first and last
            name = employee[1] + " " + employee[2]
            # creates a new SalesPerson object
            newSP = SalesPerson(int(employee[0]), name)
            # loops through the first sale to the final sale
            for sale in range(3, len(employee)):
                # stores the sales
                newSP.enterSale(float(employee[sale]))
            # adds each SalesPerson object to SalesForce list
            self.salesForce.append(newSP)

    def quotaReport(self, _quota):
        for salesPerson in self.salesForce:
            print(salesPerson)
            print("Met Quota?:", salesPerson.metQuota(_quota))
            print()

    def topSalesPerson(self):
        self.salesForce.sort(key=SalesPerson.totalSales, reverse=True)
        return self.salesForce[0]


    def individualSales(self, _id):
        # loops through the salesforce list
        for sp in self.salesForce:
            # prints if the id is found in the list
            if sp.getId() == _id:
                print("Sales: {0}\nSales Total: ${1:0.02f}".format(sp.getSales(), sp.totalSales()))
                return
        # prints if the id number doesnt exist
        print("There is no employee with this {0} ID number.".format(_id))


rex = SalesPerson(225, "Rex")
kobe = SalesPerson(2425, "Kobe")

print(rex.getPersonName())
rex.setPersonName("Rex Ferrer")
print(rex.getPersonName())
print(rex.getId())
rex.enterSale(500.25)
rex.enterSale(250.75)
print(rex.totalSales())
rex.enterSale(100.65)
print(rex.getSales())
print(rex.metQuota(1000.00))
print(rex.metQuota(300.00))
print(rex)
print(rex.compareTo(kobe))

print("**************************")

print(kobe.getPersonName())
kobe.setPersonName("Kobe Bryant")
print(kobe.getPersonName())
print(kobe.getId())
kobe.enterSale(10500.25)
kobe.enterSale(10250.75)
print(kobe.totalSales())
kobe.enterSale(1100.65)
print(kobe.getSales())
print(kobe.metQuota(1000000.00))
print(kobe.metQuota(2300.00))
print(kobe)
print(kobe.compareTo(rex))

