class student:
    school="GHSS"
    def __init__(self,roll_num,name,study_class,teacher):
        self.roll_num=roll_num
        self.name=name
        self.study_class=study_class
        self.teacher=teacher

    def display_details(self):
        print(f"name:{self.name}\nroll number:{self.roll_num}\n"
              f"class:{self.study_class}\n Teacher:{self.teacher}\n"
              f"school_name:{student.school}")
    def set_mark(self,phy,che,cs,maths):
        self.physics=phy
        self.chemistry=che
        self.cs=cs
        self.maths=maths
    def avg_mark(self):
        return(self.physics+self.chemistry+self.cs+self.maths)/4
    
s1 = student(1,"akash",9,"mini")
s1.display_details()
s1.set_mark(80,70,56,85)
print("Average Mark",s1.avg_mark())

s2=student(2,"anand","10th","omana")
s2.display_details()
s2.set_mark(60,89,92,56)
print("average mark", s2.avg_mark())