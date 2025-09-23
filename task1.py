attendence= [18,20,19,15,21]
for x in attendence:
    if x >=20:
      print("The class is full")

    else:
      print("The classis not full")

def count(attendence):
  a=0
for x in attendence:
    if x>=20:
        
          a +=1
     return x

print(count(attendence))