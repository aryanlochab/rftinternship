students = []
with open("day5.csv", "r") as file:
    #read all lines
    lines = file.readlines() 
    
    #header
    headers = lines[0].strip().split(",")

    for line in lines[1:]:
        values = line.strip().split(",")

        #dict
        student = {
            "NAME": values[0],
            "AGE":int(values[1]),
            "MARKS":int(values[2]),
        }

        students.append(student)
    

print(students)

# BONUS: average marks

total = 0

for student in students:
    total += student["MARKS"]

avg = total / len(students)

print(f"Average marks = {avg}")

