class Employee:
    raise_pay = 1.04
    count_employees = 0

    # constructor method
    def __init__(self, firstname, lastname, age, email, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.pay = pay
        Employee.count_employees += 1

    # instance method
    def get_full_name(self):
        return '{} {}'.format(self.firstname, self.lastname)

    # instance method
    def apply_raise(self):
        self.pay = int(self.raise_pay * self.pay)


emp1 = Employee('John', 'Smith', 34, 'john.smith@altermail.com', 56700)
emp2 = Employee('Kinley', 'Morris', 34, 'kinley.morris@hotmail.com', 89777)

emp1.apply_raise()
print(f"""{emp1.get_full_name()} has been promoted to get ${emp1.pay} annually""")

emp2.apply_raise()
print(f"""{emp2.get_full_name()} has been promoted to get ${emp2.pay} annually""")

print(f"""Total employees via emp1 instance: {emp1.count_employees}""")
print(f"""Total employees via emp2 instance: {emp2.count_employees}""")
print(f"""Total employees via Employee class: {emp1.count_employees}""")

print("Increasing pay for all employees to 7% after an year")
Employee.raise_pay = 1.07
emp1.apply_raise()
emp2.apply_raise()
print(f"""Employee class looks like: {Employee.__dict__}""")
print(f"""Employee 1 looks like: {emp1.__dict__}""")
print(f"""Employee 2 looks like: {emp2.__dict__}""")

print(f"""Employee 1 pay: {emp1.pay}""")
print(f"""Employee 2 pay: {emp2.pay}""")

print("Increasing pay for only Employee 1 to 10% after an year")
emp1.raise_pay = 1.10
emp1.apply_raise()
print(f"""Employee 1 pay: {emp1.pay}""")
print(f"""Employee 2 pay: {emp2.pay}""")
