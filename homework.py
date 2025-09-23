attendance= [18,20,19,15,21]
for x in attendance:
    if x >=20:
      print("The class is full")

    else:
      print("The classis not full")

# days with full attendance

def full_day(attendance):
   a = 0
   for x in attendance:
      if x >=20:
         a+=1
   return a
   
print("The full day attendance", full_day(attendance))

#Total attendance

def total_attendance(attendance):
    total = 0
    for x in attendance:
        total += x

    return total
print(total_attendance(attendance))


   