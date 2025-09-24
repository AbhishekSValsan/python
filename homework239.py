#class

class employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role

    def display(self):
        print(f"my name is {self.name} and my role is {self.role}")

class trainer(employee):
    def __init__(self, name, role, specialization):
        employee.__init__(self,name, role)
        self.specialization = specialization

    def display(self):
        print(f"my name is {self.name}, my role is {self.role} and my specialization is {self.specialization}")

class yogainstructor(employee):
    def __init__(self, name, role, yogastyle):
        employee.__init__(self,name, role)
        self.yogastyle = yogastyle

    def display(self):
        print(f"my name is {self.name}, my role is {self.role} and my yoga style is {self.yogastyle}")

class multiinstructor(trainer, yogainstructor):
    def __init__(self, name, role, specialization, yogastyle):
        trainer.__init__(self,name, role, specialization)
        yogainstructor.__init__(self,name,role, yogastyle)
        

    def display(self):
        print(f"my name is {self.name}, my role is {self.role}, my specialization is {self.specialization} and my yoga style is {self.yogastyle}")


obj=employee("midhun","coach")
obj.display()
obj1=trainer("akash","trainer","weight training")
obj1.display()
obj2=yogainstructor("reshma","yogainstructor","hatha yoga")
obj2.display()
obj3=multiinstructor("abi","multiinstructor","cardio","vinyasa yoga")
obj3.display()