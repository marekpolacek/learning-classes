class Employee:

    raise_amount = 1.04

    # constructor
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    # regular methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # class methods
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    # class methods as constructors
    @classmethod
    def from_string(cls,employee_string):
        first, last, pay = employee_string.split('-')
        return first, last, pay

    # static method
    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6):
            return False
        return True

# Exercise 1: creating instances of a class

employee_1 = Employee('Marek','Polacek',50000)
print(employee_1.fullname())

employee_2 = Employee('Test','Employee',60000)
print(employee_2.__dict__)

# Exercise 2: using class variables and methods

print(employee_1.pay)
employee_1.apply_raise()
print(employee_1.pay)

# Exercise 3: using class methods and alternative constructors

employee_3_string = 'John-Doe-40000'
first, last, pay = employee_3_string.split('-')
employee_3 = Employee(first,last,pay)

employee_4_string = 'Jane-Doe-70000'
employee_4 = Employee.from_string(employee_4_string)

# Exercise 4: using static methods

import datetime
my_date = datetime.date(2020,2,29)
print(Employee.is_workday(my_date))