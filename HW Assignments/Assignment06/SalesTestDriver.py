# SalesTestDriver.py
# Author: Pharr

# SalesTestDriver - creates a SalesForce object and uses it
# to determine aspects of the sales force.

# Your Two Classes can be added here...


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

def main():
    theSalesForce = SalesForce()
    theSalesForce.addData("salesdata.txt")
    
    print ("Quota report:")
    theSalesForce.quotaReport(750)
    print ("\n************************\n")

    topSales = theSalesForce.topSalesPerson()
    print ("Top sales person:")
    print (topSales)
    print ("\n************************\n")
    
    theSalesForce.individualSales(123)
    print ()
    theSalesForce.individualSales(999)
    print ()
    theSalesForce.individualSales(456)
    print ()
    theSalesForce.individualSales(345)

main()
