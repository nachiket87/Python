#def add(x,y):
#    return x+y
#def multiply(x,y):
#    return x * y
#def divide(x,y):
#    return x/y
#
#x = int(input("enter value of x: "))
#y = int(input("enter value of y: "))
#
#
#r = int(input("Enter radius of a circle: "))
#
#area = (r * r) * 3.143 
#
#print(area)
#



# referesher on classes

class Nachiket:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def fullname(self):
        return self.name + ' Pusalkar'

class Employee(Nachiket):
    def __init__(self,name):
        self.name = name;

x = Nachiket('Nachiket')
y = Employee('Maits')


