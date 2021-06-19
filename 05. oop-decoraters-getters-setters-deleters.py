class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.email = '{}.{}@hotmail.com'.format(first_name, last_name)

    # creating decorater property
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # creating decorater property
    @property
    def email(self):
        return '{}.{}@hotmail.com'.format(self.first_name, self.last_name).lower()

    # creating decorater setter
    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(" ")
        self.first_name = first_name
        self.last_name = last_name

    # creating decorater deleter
    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None


emp1 = Employee('Corey', 'Anderson')

print("Employee firstname: " + emp1.first_name)
print("Employee fullname: " + emp1.full_name)
print("Employee email: " + emp1.email)

print("\nUpdating first name --> \n")
emp1.first_name = 'James'
print("Employee firstname: " + emp1.first_name)
print("Employee fullname: " + emp1.full_name)
print("Employee email: " + emp1.email)

# using decorater setter
print("\nSetting Employee fullname --> \n")
emp1.full_name = 'Black Sabbath'
print("Employee firstname: " + emp1.first_name)
print("Employee fullname: " + emp1.full_name)
print("Employee email: " + emp1.email)

# using decorater deleter
del emp1.full_name
print("Employee firstname: " + str(emp1.first_name))
print("Employee fullname: " + str(emp1.full_name))
print("Employee email: " + str(emp1.email))
