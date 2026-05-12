import csv

student = []
topper = {}

math_total = 0
science_total = 0
english_total = 0 
with open("day7.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        
        name = row['NAME']
        math = int(row['MATH'])
        science = int(row['SCIENCE'])
        english = int(row['ENGLISH'])
        avg_per_student = (math + science + english)/3
        all_total = math + science + english
        topper[name] = all_total
        student.append({
            "NAME": name,
            "MATH": math,
            "SCIENCE": science,
            "ENGLISH": english, 
            "AVERAGE" : avg_per_student,   
        })

        len(student)
        
        #total marks
        math_total += math
        english_total += english
        science_total += science

        #avg subject wise
        math_avg = math_total/len(student)
        english_avg = english_total/len(student)
        science_avg = science_total/len(student)

#topper 
topper_name = max(topper, key=topper.get)
print(f"The topper was {topper_name}")

#avg marks per student 
for row in student:
    print(f"The average marks of {row['NAME']} is {row['AVERAGE']}")
    
#students above avg
for row in student:
    if row["MATH"] > math_avg:
        print(f"{row["NAME"]} scored above avg in maths")
    if row["SCIENCE"] > science_avg:
        print(f"{row["NAME"]} scored above avg in science")
    if row["ENGLISH"] > english_avg:
        print(f"{row["NAME"]} scored above avg in english")

#GRADE

    


        
