class Employee:
    
    def __init__(self,first,second,pay):
        self.first = first
        self.second = second
        self.pay = pay
        self.emp_1 = first + second + '@gmail.com'
        self.emp_2 = first + '.' + second + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.second)

emp_1  = Employee('sunil','giri','50000')
emp_2  = Employee('test','user','60000')

# print(emp_1)
# print(emp_2)

print(emp_1.emp_1) 
print(emp_2.emp_2)

print(emp_2.fullname())