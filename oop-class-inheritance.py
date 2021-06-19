class Employee:
    raise_perc = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}.{}@ymail.com'.format(first_name, last_name)
        self.pay = pay

    def apply_raise(self):
        self.pay = self.raise_perc * self.pay

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp1 = Employee('Aaron', 'Smith', 40000)
emp2 = Employee('Chris', 'Morris', 70000)

print(emp1.email, emp2.email)
print()


# new class Developer inheriting from Employee
class Developer(Employee):
    raise_perc = 1.10

    def __init__(self, first_name, last_name, pay, skillset):
        super().__init__(first_name, last_name, pay)
        self.skillset = skillset


dev1 = Developer('Dunkin', 'Donut', 50000, 'Python')
dev2 = Developer('Lorry', 'Narsik', 70000, 'Java')

# print(help(dev1))

print(f"""Developer 1 salary before raise: {dev1.pay}""")
print(f"""Developer 2 salary before raise: {dev2.pay}""")
dev1.apply_raise()
dev2.apply_raise()
print(f"""Developer 1 salary after raise: {dev1.pay}""")
print(f"""Developer 1 salary after raise: {dev2.pay}""")


# new class Manager inheriting from Employee
class Manager(Employee):

    def __init__(self, first_name, last_name, pay, reportees=None):
        super().__init__(first_name, last_name, pay)
        if reportees == None:
            self.reportees = []
        else:
            self.reportees = reportees

    def add_reportee(self, reportee):
        if reportee not in self.reportees:
            self.reportees.append(reportee)

    def remove_reportee(self, reportee):
        if reportee in self.reportees:
            self.reportees.remove(reportee)

    def show_hierarchy(self):
        print(f"""{self.get_full_name()} has reportees --> """)
        for emp in self.reportees:
            print(f"""      {emp.get_full_name()}""")


mgr = Manager('Geny', 'Clark', 98000, [dev1, dev2])

mgr.show_hierarchy()

dev3 = Developer('George', 'Ruskin', 77000, 'Coreldraw')
dev4 = Developer('Garry', 'Larson', 55000, 'Golang')

print("Adding two developers under Manager")
mgr.add_reportee(dev3)
mgr.add_reportee(dev4)
print("Manager latest reporting hierarchy")
mgr.show_hierarchy()

print("Removing two developers under Manager")
mgr.remove_reportee(dev1)
mgr.remove_reportee(dev2)
print("Manager latest reporting hierarchy")
mgr.show_hierarchy()

# using instance or class verify methods
print(f"""Manager instance of Employee ? : {isinstance(mgr, Employee)}""")
print(f"""Developer instance of Employee ? : {isinstance(dev1, Employee)}""")
print(f"""Manager instance of Developer ? : {isinstance(mgr, Developer)}""")

print(f"""Manager subclass of Employee ? : {issubclass(Manager, Employee)}""")
print(f"""Developer subclass of Employee ? : {issubclass(Developer, Employee)}""")
print(f"""Manager subclass of Developer ? : {issubclass(Manager, Developer)}""")
