class Address:
    def __init__(self,cy,st,pc):
        self.city = cy
        self.state = st
        self.pincode = pc 
    
    def display(self):
        return f'''
              City          : {self.city}
              State         : {self.state}
              Pincode       : {self.pincode}
            ''' 
class Employee :
    def __init__(self,eid,nm,dp,bs,ad):
        self.employee_id =eid
        self.name = nm
        self.department = dp 
        self.__basic_salary = bs
        self.address = ad
        
        self.set_salary(bs)
 
    def get_salary(self):
        return self.__basic_salary
        
    def set_salary(self,salary):
        if salary >= 10000:
            self.__basic_salary = salary
        else:
            print("basic salary cannot be less than RS. 10,000")    
                
    def calculate_salary(self):
        return self.__basic_salary 
    
    def display(self):
        print(f'''
              Employee Id   : {self.employee_id}
              Employee Name : {self.name}
              Department    : {self.department}
              Basic Salary  : {self.get_salary()}
              Final Salary  : {self.calculate_salary()}
              Address       : {self.address.display()}
              ''')    
       
    def __str__(self):
        return f"{self.employee_id} - {self.name} - {self.department}"   

class Developer(Employee) :
    def __init__(self,eid,nm,dp,bs,ad,technology):
        super().__init__(eid,nm,dp,bs,ad)
        self.technology = technology
    def calculate_salary(self):
        return self.get_salary() + 5000     
    
    def display(self):

         print(f'''
                Employee Id   : {self.employee_id}
                Employee Name : {self.name}
                Department    : {self.department}
                Basic Salary  : {self.get_salary()}
                Bonus         : 5000
                Final Salary  : {self.calculate_salary()}
                Technology    : {self.technology}
                City          : {self.address.city}
            ''')
        
        
class Tester(Employee) :
    def __init__(self,eid,nm,dp,bs,ad,testing_type):
        super().__init__(eid,nm,dp,bs,ad)
        self.testing_type = testing_type
    def calculate_salary(self):
        return self.get_salary() + 3000     
    
    def display(self):

         print(f'''
                Employee Id   : {self.employee_id}
                Employee Name : {self.name}
                Department    : {self.department}
                Basic Salary  : {self.get_salary()}
                Bonus         : 3000
                Final Salary  : {self.calculate_salary()}
                Testing Type    : {self.testing_type}
                City          : {self.address.city}
            ''')
        
 
class Manager(Employee) :
    def __init__(self,eid,nm,dp,bs,ad,team_size):
        super().__init__(eid,nm,dp,bs,ad)
        self.team_size = team_size
    def calculate_salary(self):
        return self.get_salary() + 10000     
    
    def display(self):

         print(f'''
                Employee Id   : {self.employee_id}
                Employee Name : {self.name}
                Department    : {self.department}
                Basic Salary  : {self.get_salary()}
                Bonus         : 10000
                Final Salary  : {self.calculate_salary()}
                Team Size     : {self.team_size}
                City          : {self.address.city}
            ''') 
 
        
address1 = Address("Pune", "Maharashtra", 411001)

dev1 = Developer(
    101,
    "Rahul",
    "Development",
    40000,
    address1,
    "Python"
)

dev1.display()     
 
print("=" * 80) 

address2 = Address("Mumbai", "Maharashtra", 400001)   
tester1 = Tester(
    102,
    "Priya",
    "Testing",
    35000,
    address2,
    "Automation"
)   

tester1.display()

print("=" * 80) 

address3 = Address("Pune", "Maharashtra", 411002)

manager1 = Manager(
    103,
    "Amit",
    "Management",
    60000,
    address3,
    8
)

manager1.display()

print("=" * 80) 

employees = [dev1, tester1, manager1]

for emp in employees:
    print(emp.calculate_salary())

