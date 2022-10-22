"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, is_hourly=True, hours_worked=0, salary_pay=0, contract_number=0, contract_pay=0):
        self.name = name
        self.is_hourly = is_hourly
        self.hours_worked = hours_worked
        self.salary_pay = salary_pay
        self.contract_number = contract_number
        self.contract_pay = contract_pay

    def get_pay(self):
        return (self.hours_worked * self.salary_pay) + (self.contract_pay * self.contract_number)

    def __str__(self):
        if self.is_hourly and self.hours_worked > 1:
            workType = "contract"
            amount = "{} hours at {}/hour".format(self.hours_worked, self.salary_pay)
        else:
            workType = "monthly salary"
            amount = "{}".format(self.salary_pay)

        if self.contract_number > 1 and self.contract_pay > 0:
            contractStatment = " and receives a commission for {} contract(s) at {}/contract".format(self.contract_number, self.contract_pay)
            amount+=contractStatment
        elif self.contract_number == 1:
            contractStatment = " and receives a bonus commission of {}".format(self.contract_pay)
            amount+=contractStatment

        endingStatement = " Their total pay is " + str(self.get_pay())
        return "{} works on a {} of {}. {}.".format(self.name, workType, amount, endingStatement)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', is_hourly=False, hours_worked=1, salary_pay=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', is_hourly=True, hours_worked=100, salary_pay=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', is_hourly=False, hours_worked=1, salary_pay=3000, contract_number=4, contract_pay=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', is_hourly=True, hours_worked=150, salary_pay=25, contract_number=3, contract_pay=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', is_hourly=False, hours_worked=1, salary_pay=2000, contract_number=1, contract_pay=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', is_hourly=True, hours_worked=120, salary_pay=30, contract_number=1, contract_pay=600)
