def companyName():
    # user's input
    domain = input('Provide the domain name of a company(i.e. www.target.com): ')

    # splits the string domain at '.'
    company = domain.split('.')

    # prints the 2nd object in the company list
    print(company[1])
companyName()
