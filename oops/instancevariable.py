class Employee:
    company_name = "Tech Corp"  # Class variable
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02

    def showDetails(self):
        print(f"Name: {self.name} & raise amount is {self.raise_amount} & company name is {self.company_name}")


emp1 = Employee("John")
emp1.raise_amount = 0.05  # This will change the raise amount for emp1 only
emp1.company_name = "Tech Innovations"  # This will change the company name for emp1 only
emp1.showDetails()

# Employee.showDetails(emp1)  # This is equivalent to emp1.showDetails()
emp2 = Employee("Jane")
emp2.showDetails()