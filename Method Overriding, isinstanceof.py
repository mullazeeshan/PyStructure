
'''
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
'''

'''
class one:
    def number(self,a,b):
        self.a=a
        self.b=b

class add(one):
    def sum(self):
        self.plus=self.a+self.b
        print(self.plus)
class sub(one):
    def diff(self):
        self.minus=self.a-self.b
        print(self.minus)
class result(add,sub):
    def answer(self):
        print("answer of sum %d and difference %d " %(self.plus,self.minus))
a1=result()
#a = int(input("enter a: "))
#b = int(input("enter b: "))
a1.number(3,1)
a1.sum()
a1.diff()
a1.answer()

'''
class Teacher:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Student(Teacher):
    def __init__(self,name,id,age):
        #Teacher.__init__(self,name,id) #works same
        super().__init__(name,id) #works same
        self.age=age
    def display(self):
        print("name",self.name)
        print("id:",self.id)
        print("age:",self.age)

s=Student('abc',12,1)
s.display()


class Bank:
    def getroi(self):
        return 10;
class SBI(Bank):
    def getrom(self):
        return 7;
class ICICI(Bank):
    def getron(self):
        return 8;
b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi());
print("SBI Rate of interest:", b2.getrom());
print("ICICI Rate of interest:", b3.getron());

print(isinstance(b1,Bank))
print(issubclass(SBI,Bank))



