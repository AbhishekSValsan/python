attendance = [18, 20, 19, 15, 21]

# Check attendance each day

for x in attendance:
    if x >= 20:
        print("Full Attendance")
    else:
        print("Not Full")

# Count days with full attendance
def fullClassCount(attendance):
    a = 0
    for y in attendance:
        if y >= 20:
            a += 1
    return a
print("Full Day Count:", fullClassCount(attendance))

#total attendance

def total_attendance(attendance):
    total = 0
    for x in attendance:
        total=+x

    return total
print(total_attendance(attendance))


