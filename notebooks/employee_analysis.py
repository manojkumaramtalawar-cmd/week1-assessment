#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis — Week 1 Assessment
# 
# ## Project Objective
# Analyse employee data using NumPy, Pandas and Matplotlib.
# 
# ## Objectives
# - Load and explore employee data.
# - Handle missing values and duplicate records.
# - Analyse department-wise salaries and headcount.
# - Merge employee and department datasets.
# - Visualise employee salary patterns.

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

print("Libraries imported successfully")


# ## 1. Load Employee Dataset
# Load the employee dataset and display the first five records.

# In[19]:


root = Path.cwd()

if not (root / "data").exists():
    root = root.parent

df = pd.read_csv(root / "data" / "employees.csv")

df.head()


# ## 2. Data Exploration
# Examine the dataset structure, data types, missing values
# and duplicate records.

# In[20]:


print("Dataset Shape:", df.shape)

print("\nDataset Information:")
df.info()

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())


# ## 3. Performance Measurement
# Use the Jupyter %timeit magic command to measure
# the execution time of a salary calculation.

# In[21]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# ## 4. NumPy Array Analysis
# 
# Analyse student marks using NumPy arrays, averages,
# broadcasting and weighted scores.

# In[22]:


marks = np.array([
    [75, 80, 85],
    [65, 70, 75],
    [90, 85, 95],
    [60, 75, 80]
])

print("Marks:\n", marks)
print("Shape:", marks.shape)
print("Student Averages:", marks.mean(axis=1))
print("Subject Averages:", marks.mean(axis=0))

print("\nAfter Adding 5 Grace Marks:")
print(marks + 5)

weights = np.array([0.3, 0.3, 0.4])

print("\nWeighted Scores:")
print(np.dot(marks, weights))


# ## 5. Data Cleaning
# 
# - Identify missing values.
# - Fill missing salaries using the median.
# - Remove duplicate records.
# - Correct data types.
# - Standardise text values.

# In[23]:


df_missing = pd.read_csv(
    root / "data" / "employees_missing.csv"
)

print("Before Cleaning:")
print("Shape:", df_missing.shape)

print("\nMissing Values:")
print(df_missing.isna().sum())

print("\nDuplicate Records:")
print(df_missing.duplicated().sum())

df_missing.head()


# In[24]:


df_clean = df_missing.copy()

# Convert salary to numeric
df_clean["salary"] = pd.to_numeric(
    df_clean["salary"], errors="coerce"
)

# Fill missing salaries with median
median_salary = df_clean["salary"].median()

df_clean["salary"] = df_clean["salary"].fillna(
    median_salary
)

# Standardise text columns
for col in ["name", "department", "city"]:
    df_clean[col] = df_clean[col].str.strip().str.title()

# Remove duplicate records
df_clean = df_clean.drop_duplicates().reset_index(drop=True)

print("Data Cleaning Completed")
print("Median Salary:", median_salary)

df_clean


# In[25]:


print("After Cleaning:")
print("Shape:", df_clean.shape)

print("\nMissing Values:")
print(df_clean.isna().sum())

print("\nDuplicate Records:")
print(df_clean.duplicated().sum())


# ## 6. Department-wise Analysis
# 
# Calculate employee headcount, average salary and maximum
# salary for each department using groupby and aggregation.

# In[26]:


# Standardise department names
df_clean["department"] = df_clean["department"].str.upper()

department_summary = df_clean.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
).reset_index()

department_summary


# ## 7. Dataset Merging
# 
# Combine employee and department datasets using inner,
# left and outer joins.
# 
# Identify departments that have no employees.

# In[27]:


departments = pd.read_csv(
    root / "data" / "departments.csv"
)

departments["department"] = (
    departments["department"].str.strip().str.upper()
)

departments


# In[28]:


inner_join = pd.merge(
    df_clean,
    departments,
    on="department",
    how="inner"
)

print("Inner Join:")
inner_join


# In[29]:


left_join = pd.merge(
    df_clean,
    departments,
    on="department",
    how="left"
)

print("Left Join:")
left_join


# In[30]:


outer_join = pd.merge(
    df_clean,
    departments,
    on="department",
    how="outer",
    indicator=True
)

print("Outer Join:")
outer_join


# In[31]:


no_employees = outer_join.loc[
    outer_join["_merge"] == "right_only",
    ["department", "head", "budget", "bonus"]
]

print("Departments with no employees:")
print(no_employees.to_string(index=False))


# In[32]:


print(departments.columns.tolist())
print(outer_join.columns.tolist())


# ## 8. Data Visualisation
# 
# Visualise employee salary distribution, department-wise
# average salaries and salary patterns using Matplotlib.

# In[33]:


charts_path = root / "reports" / "charts"
charts_path.mkdir(parents=True, exist_ok=True)

plt.style.use("ggplot")


# In[34]:


plt.figure(figsize=(8, 5))

plt.bar(
    department_summary["department"],
    department_summary["average_salary"],
    color="steelblue",
    label="Average Salary"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.legend()
plt.tight_layout()

plt.savefig(charts_path / "department_salary_bar.png")
plt.show()


# **Insight:** The bar chart helps identify which department
# has the highest and lowest average salary.

# In[35]:


plt.figure(figsize=(8, 5))

plt.hist(
    df_clean["salary"],
    bins=5,
    color="steelblue",
    edgecolor="black",
    label="Employee Salaries"
)

plt.title("Employee Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()

plt.savefig(charts_path / "salary_histogram.png")
plt.show()


# **Insight:** The histogram shows how employee salaries
# are distributed across different salary ranges.

# In[36]:


plt.figure(figsize=(8, 5))

plt.scatter(
    df_clean["id"],
    df_clean["salary"],
    color="steelblue",
    s=80,
    label="Employee Salary"
)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend()
plt.tight_layout()

plt.savefig(charts_path / "salary_scatter.png")
plt.show()


# **Insight:** The scatter plot highlights differences
# in salary among individual employees.

# In[37]:


sorted_salary = df_clean["salary"].sort_values().reset_index(drop=True)

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, len(sorted_salary) + 1),
    sorted_salary,
    marker="o",
    color="steelblue",
    label="Sorted Salary"
)

plt.title("Employee Salaries in Ascending Order")
plt.xlabel("Employee Rank")
plt.ylabel("Salary (INR)")
plt.legend()
plt.tight_layout()

plt.savefig(charts_path / "salary_line.png")
plt.show()


# **Insight:** The line chart shows the salary gap
# between the lowest-paid and highest-paid employees.

# 
