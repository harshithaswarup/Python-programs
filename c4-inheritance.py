# multilevel inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showname(self):
        print self.name
        return self.name

    def showage(self):
        print self.age
        return self.age
class Employee(Person):
    def __init__(self,name,age,e_no):
        Person.__init__(self,name,age)
        self.e_no=e_no

    def showemp(self):
        print self.e_no
        return self.e_no
class Employee2(Employee):
    def __init__(self,name,age,e_no,e_salary):
        Employee.__init__(self,name,age,e_no)
        self.e_salary=e_salary

    def showsal(self):
        print self.e_salary
        return self.e_salary
p=Person("h",21)
p.showname()
p.showage()
e=Employee("a",1,"e2")
e.showemp()
e.showname()
e.showage()
e1=Employee2("x",2,"e3",10000)
e1.showname()
e1.showage()
e1.showemp()
e1.showsal()

