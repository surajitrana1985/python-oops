class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}.{}@yahoomail.co.in'.format(first_name, last_name)
        self.pay = pay

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # creating dunder or magic method (fallback if method __str__ not present) - used for debugging
    def __repr__(self):
        return 'Employee({''}, {''}, {})'.format(self.first_name, self.last_name, self.pay)

    # creating dunder or magic method - (overrides __repr__ method) used for users
    def __str__(self):
        return '{} - {}'.format(self.get_full_name(), self.email.lower())

    # creating dunder method to add pay of all employees
    def __add__(self, other):
        return self.pay + other.pay

    # creating dunder method to find the length of fullnames
    def __len__(self):
        return len("".join(self.get_full_name().split(" ")))


emp1 = Employee('Colin', 'Anderson', 12000)
print(emp1)

emp2 = Employee('Andrew', 'Plew', 17000)
print(emp2)

add_pay = emp1 + emp2
print("Total pay of all employees: $" + str(add_pay))

print("Length of fullname characters of Employee 1: " + str(len(emp1)))
print("Length of fullname characters of Employee 2: " + str(len(emp2)))

print(1 + 2)
print(int.__add__(1, 2))

print('a' + 'b')
print(str.__add__('a', 'b'))
