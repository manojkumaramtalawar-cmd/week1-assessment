
# calculate bonus
def bonus(salary, rate=0.1, *extras, **options):
    total_bonus = salary * rate + sum(extras)

    if "cap" in options:
        total_bonus = min(total_bonus, options["cap"])

    return total_bonus


print("Bonus:", bonus(50000))
print("Bonus with extras:", bonus(50000, 0.1, 1000, 2000))
print("Bonus with cap:", bonus(50000, 0.1, 1000, cap=6000))


# Custom exception for invalid salary
class InvalidSalaryError(Exception):
    pass


# Parent class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


# Child class
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager: {self.name}, Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )
        
# Testing Employee
employee = Employee("Arun", 30000)

print(employee.get_details())
print("Annual salary:", employee.annual_salary())

# Testing Manager
manager = Manager("Priya", 80000, 5)

print(manager.get_details())
print("Annual salary:", manager.annual_salary())

# custom exception
try:
    invalid_employee = Employee("Test", -500)

except InvalidSalaryError as error:
    print("Error:", error)

finally:
    print("Transaction finished")
    
# Employee data for list comprehension, map and filter
employees = [
    {"name": "Arun", "salary": 30000, "city": "Chennai"},
    {"name": "Priya", "salary": 45000, "city": "Chennai"},
    {"name": "Rahul", "salary": 60000, "city": "Bangalore"},
    {"name": "Divya", "salary": 75000, "city": "Chennai"},
    {"name": "Karthik", "salary": 90000, "city": "Mumbai"},
    {"name": "Meena", "salary": 52000, "city": "Bangalore"},
    {"name": "Suresh", "salary": 68000, "city": "Chennai"},
    {"name": "Anitha", "salary": 48000, "city": "Mumbai"},
]

# List comprehension
high_salary_names = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 50000
]

print("Above 50000:", high_salary_names)

# map and lambda - increase salary by 10%
raised_salaries = list(
    map(lambda employee: employee["salary"] * 1.10, employees)
)

print("Raised salaries:", raised_salaries)

# filter - keep only Chennai employees
chennai_employees = list(
    filter(lambda employee: employee["city"] == "Chennai", employees)
)

chennai_names = [employee["name"] for employee in chennai_employees]

print("Chennai:", chennai_names)

# Loop with continue and break
salaries = [30000, 45000, 0, 60000, 90000, 52000]

for salary in salaries:

    if salary == 0:
        continue

    print("Processing salary:", salary)

    if salary > 85000:
        print("Salary above 85000 found. Stopping.")
        break