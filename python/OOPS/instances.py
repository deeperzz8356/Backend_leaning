class Employee:
    emp_no=0
    raise_amt=1.04
    def __init__(self,first,last,sal):
        self.first=first
        self.last=last
        self.sal=sal
        self.email=first + '.' + last + '@company.com'
        Employee.emp_no +=1
        
    
    def fullname(self):
        return " {} {}".format(self.first,self.last)
    def raisesal(self):
        self.sal= self.sal* self.raise_amt
        return self.sal
    
    @classmethod
    def isemp(cls,emp_str):
        first,last,sal=emp_str.split('-')
        return cls(first,last,sal)
    
emp_1=Employee('Deep','Pandey',60000)
emp_2=Employee('Test','User',50000)
emp_str='jhon-doe-1000'
emp_3=Employee.isemp(emp_str)

print(Employee.emp_no)
print(emp_1.raisesal())

print(emp_2.fullname())
print(Employee.fullname(emp_1))
print(emp_1.email)
print(emp_3.email)

        