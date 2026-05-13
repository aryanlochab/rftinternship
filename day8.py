
import csv

employees = []

# grouping dictionaries
department_salary = {}
highest_paid = {}

with open("day8.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = row["NAME"]
        dept = row["DEPT"]
        salary = int(row["SALARY"])

        # store employee data
        employees.append({
            "NAME": name,
            "DEPT": dept,
            "SALARY": salary
        })

        # GROUPBY logic
        if dept not in department_salary:
            department_salary[dept] = []

        department_salary[dept].append(salary)

        # highest paid employee per department
        if dept not in highest_paid:

            highest_paid[dept] = {
                "NAME": name,
                "SALARY": salary
            }

        elif salary > highest_paid[dept]["SALARY"]:

            highest_paid[dept] = {
                "NAME": name,
                "SALARY": salary
            }

# average salary per department

print("Average Salary Per Department:\n")

department_avg = {}

#.will complete