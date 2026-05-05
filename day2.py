marks = [75, 85, 90, 67, 85, 92, 78]

# basic stats
numofval = len(marks)
highest_val = max(marks)
lowest_value = min(marks)

# total
total = sum(marks)

# average
avg = total / numofval

print(f"Average score = {avg}")
print(f"Highest score = {highest_val}")
print(f"Lowest score = {lowest_value}")

# students above average
def above_avg():
    count = 0
    for mark in marks:
        if mark > avg:
            count += 1
    return count

result = above_avg()
print(f"Students above average: {result}")

#BONUS

# grade distribution
def grade_distribution():
    grd_dis = {"A": 0, "B": 0, "C": 0, "Fail": 0}
    
    for mark in marks:
        if mark >= 80:
            grd_dis["A"] += 1
        elif mark >= 70:
            grd_dis["B"] += 1
        elif mark >= 60:
            grd_dis["C"] += 1
        else:
            grd_dis["Fail"] += 1
    
    return grd_dis

result1 = grade_distribution()
print(f"Grade distribution: {result1}")

#some insights

#spread

spread = highest_val - lowest_value

if spread > 20:
    print("Performance of class is inconsistent")
else:
    print("Performance of class is consistent")

#extremes

top_students = [m for m in marks if m >= 90]
weak_students = [m for m in marks if m < 70]
print(f"top students marks =  {top_students}")
print(f"weak students marks =  {weak_students}")