class Personal:
    def _init_(self,name,phno,email):
        self.name=name
        self.phno=phno
        self.email=email
    def display(self):
        print(self.name,self.phno,self.email)
class Student(Personal):
    def _init_(self,name,phno,email,rollno,college,branch):
        self.rollno=rollno
        self.college=college
        self.branch=branch
        super()._init_(name,phno,email)
    def display(self):
        print(self.rollno,self.college,self.branch)
        super().display()
class Employee(Personal):
    def _init_(self,name,phno,email,empid,empsal):
        self.empid=empid
        self.empsal=empsal
        super()._init_(name,phno,email)
    def display(self):
        print(self.empid,self.empsal)
        super().display()
s1=Student("revathi",9912358548,"revathi@gmail.com",123,"Aditya","Cse")
s1.display()
e1=Employee("revathi",9110511218,"polavarfapurevathi@gmail.com",11,40000)
e1.display()
