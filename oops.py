class employee:
    company_name="ABC TECHNOLIGIES"
    location="Kochi"
    def __init__(self,id,name,salary):
       self.emp_id=id
       self.emp_name=name
       self.emp_salary=salary

    def get_details(self):
        print(self.emp_id,self.emp_name,self.emp_salary)

obj1=employee(101,"midhun",25000)
obj2=employee(102,"akash",50000)
obj3=employee(103,"reshma",26000)

obj1.get_details() 
obj2.get_details()
obj3.get_details()
    

