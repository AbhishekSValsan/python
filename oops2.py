class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
         print("Hi I'm",self.name)
         print("Hi I'm",self.age)

    def info1(self):
         print(f"my name is {self.name} and my age is {self.age}")

obj=student("midhun",22)
obj.intro()
obj.info1()
obj1=student("akash",21)
obj1.intro()
obj1.info1()
obj2=student("reshma",20)
obj2.intro()
obj2.info1()
