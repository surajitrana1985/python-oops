import datetime


class Employee:
    raise_pay = 1.04

    # constructor method
    def __init__(self, first_name, last_name, email, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pay = pay
        self.timestamp = Employee.get_timestamp()

    # instance method
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # instance method
    def apply_raise(self):
        self.pay = self.raise_pay * float(self.pay)

    # class method
    @classmethod  # decorator
    def from_string(cls, employee_str):
        fname, lname, email, pay = employee_str.split("-")
        return cls(fname, lname, email, pay)

    # class method
    @classmethod
    def set_raise(cls):
        cls.raise_pay = 1.07

    # static method
    @staticmethod  # decorator
    def get_timestamp():
        return datetime.datetime.now()


emp1 = Employee.from_string("Jason-Gibbs-jason.gibbs@hotmail.com-36000")
emp2 = Employee.from_string("Mason-Storm-mason.storm@gmail.com-45000")
emp3 = Employee.from_string("Kelvin-Hobbs-kelvin.hobbs@yahoomail.com-89000")

Employee.set_raise()

emp1.apply_raise()
emp2.apply_raise()
emp3.apply_raise()

print("Employee 1 fullname is:", emp1.get_full_name(), "created at", emp1.timestamp, "salary is $", float(emp1.pay))
print("Employee 2 fullname is:", emp2.get_full_name(), "created at", emp2.timestamp, "salary is $", float(emp2.pay))
print("Employee 3 fullname is:", emp3.get_full_name(), "created at", emp3.timestamp, "salary is $", float(emp3.pay))
