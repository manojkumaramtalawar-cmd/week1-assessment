
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Find project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load dataset
file_path = BASE_DIR / "data" / "employees_missing.csv"

df = pd.read_csv(file_path)

# Display dataset
print("First 5 rows:")
print(df.head())

# Dataset shape
print("\nShape:")
print(df.shape)

# Dataset information
print("\nInfo:")
df.info()

# Statistical summary
print("\nDescribe:")
print(df.describe())

# Missing values
print("\nMissing values:")
print(df.isna().sum())

# Duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Data cleaning

# Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print("Duplicates:", df.duplicated().sum())

# Fill missing salaries using median
median_salary = df["salary"].median()

df["salary"] = df["salary"].fillna(median_salary)

print("\nMedian salary:", median_salary)
print("\nMissing values after cleaning:")
print(df.isna().sum())

print("\nCleaned dataset:")
print(df)

# NumPy operations

# Marks of 4 students in 3 subjects
marks = np.array([
    [80, 75, 90],
    [65, 70, 85],
    [90, 88, 95],
    [55, 60, 70]
])

print("\nMarks array:")
print(marks)

# Shape of array
print("\nShape:", marks.shape)

# Student averages 
student_averages = marks.mean(axis=1)
print("\nStudent averages:", student_averages)

# Subject averages 
subject_averages = marks.mean(axis=0)
print("\nSubject averages:", subject_averages)

# Broadcasting - add 5 grace marks
grace_marks = marks + 5
print("\nMarks after grace marks:")
print(grace_marks)

# Weighted score using np.dot
weights = np.array([0.4, 0.3, 0.3])

weighted_scores = np.dot(marks, weights)
print("\nWeighted scores:", weighted_scores)

# Pandas operations

# loc - select rows using index labels
print("\nUsing loc:")
print(df.loc[0:2, ["name", "salary"]])

# iloc - select rows using integer positions
print("\nUsing iloc:")
print(df.iloc[0:3, 0:4])

# Filtering - employees with salary above 60000
high_salary = df[df["salary"] > 60000]

print("\nEmployees with salary above 60000:")
print(high_salary)

# Groupby - average salary by department
department_salary = df.groupby("department")["salary"].mean()
# Department aggregation
department_summary = df.groupby("department").agg(
    employee_count=("name", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)


print("\nDepartment Summary:")
print(department_summary)
print("\nAverage salary by department:")
print(department_salary)


# Load department data
department_info = pd.read_csv(BASE_DIR / "data" / "departments.csv")

# Inner Join
inner_join = pd.merge(df, department_info, on="department", how="inner")

print("\nInner Join:")
print(inner_join)

# Left Join
left_join = pd.merge(df, department_info, on="department", how="left")

print("\nLeft Join:")
print(left_join)

# Outer Join
outer_join = pd.merge(df, department_info, on="department", how="outer")

print("\nOuter Join:")
print(outer_join)

# Matplotlib visualizations

# Create charts folder if it doesn't exist
charts_dir = BASE_DIR / "reports" / "charts"
charts_dir.mkdir(parents=True, exist_ok=True)


# Chart 1 - Bar chart (Average salary by department)
avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar", label="Average Salary")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.legend()
plt.tight_layout()

plt.savefig(charts_dir / "department_salary_bar.png")
plt.show()

print("Insight: IT and Finance have higher average salaries than HR and Sales.")


# Chart 2 - Histogram (Salary distribution)
plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, label="Employee Salaries")

plt.title("Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()

plt.savefig(charts_dir / "salary_histogram.png")
plt.show()

print("Insight: The histogram shows how employee salaries are distributed across salary ranges.")


# Chart 3 - Scatter plot (Salary vs Employee ID)
plt.figure(figsize=(8, 5))

plt.scatter(df["id"], df["salary"], label="Employees")

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend()
plt.tight_layout()

plt.savefig(charts_dir / "salary_scatter.png")
plt.show()

print("Insight: The scatter plot shows how salary values vary across employee records.")


# Chart 4 - Line chart (Salary by employee)
plt.figure(figsize=(8, 5))

plt.plot(df["name"], df["salary"], marker="o", label="Salary")

plt.title("Employee Salary Trend")
plt.xlabel("Employee Name")
plt.ylabel("Salary (INR)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig(charts_dir / "salary_line.png")
plt.show()

print("Insight: The line chart compares salary values across employees.")