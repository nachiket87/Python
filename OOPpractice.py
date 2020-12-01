class Employee():
    pay_increase = 1.04
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.fullname = self.fname + ' ' + self.lname

    def pay_increase(self):
        return self.salary * 1.04
    
    def __str__(self):
        return salary = self.fullname + ' is an employee of this firm'



n = Employee('Nachiket', 'Pusalkar', 10000)

n.pay_increase()

print(n.salary())