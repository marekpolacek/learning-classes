class Employee:

    # class variables
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

# Exercise 1: Creating instances of a class

employee_1 = Employee('Marek','Polacek',50000)
print(employee_1.fullname())

employee_2 = Employee('Test','Employee',60000)
print(employee_2.__dict__)

# Exercise 2: Using class variables and methods

print(employee_1.pay)
employee_1.apply_raise()
print(employee_1.pay)

# Exercise 3: Using class methods and alternative constructors

employee_3_string = 'John-Doe-40000'
first, last, pay = employee_3_string.split('-')
employee_3 = Employee(first,last,pay)
print(employee_3)

employee_4_string = 'Jane-Doe-70000'
employee_4 = Employee.from_string(employee_4_string)
print(employee_4)

# Exercise 4: Using static methods

import datetime
my_date = datetime.date(2020,2,29)
print(Employee.is_workday(my_date))

# Exercise 5: Inheritance

class Developer(Employee):

    raise_amount = 1.10

    def __init__(self,first,last,pay,programming_language):
        super().__init__(first,last,pay)
        self.programming_language = programming_language

developer_1 = Developer('Marek','Polacek',50000,'Python')
print(help(Developer))

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print('-->', employee.fullname())

manager_1 = Manager('Sue','Smith',80000,[employee_1])
print(manager_1.email)
manager_1.print_employees()

manager_1.add_employee(employee_2)
manager_1.print_employees()

# Exercise 6: isinstance and issubclass

print(isinstance(manager_1,Manager)) # true
print(isinstance(manager_1,Employee)) # true
print(isinstance(manager_1,Developer)) # false

print(issubclass(Developer,Employee)) # true
print(issubclass(Manager,Employee)) # true
print(issubclass(Manager,Developer)) # false

# Exercise 7: Special methods - dunder

class SpecialDeveloper(Developer):

    def __init__(self,first,last,pay,programming_language):
        super().__init__(first,last,pay,programming_language)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    # arithmetic dunder methods
    # add, sub, mul, ...
    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
            return len(self.fullname())

special_1 = SpecialDeveloper('Special','Developer',90000,'Python')
special_2 = SpecialDeveloper('Second','Special Developer',100000,'Python')
print(special_1)
print(repr(special_1))
print(str(special_1))
print(special_1+special_2)

print(len(special_1))