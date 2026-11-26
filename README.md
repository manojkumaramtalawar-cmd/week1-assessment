# Week 1 Assessment

## Project Overview

This project demonstrates Python programming, object-oriented programming, exception handling, file handling, REST APIs, NumPy, Pandas, Matplotlib, Jupyter Notebook and Git.

The objective is to analyse employee data, clean missing and duplicate records, compare department salaries and generate meaningful visualisations.

## Task 1 – Python Core, OOP and Errors

- Functions, default arguments, *args and **kwargs.
- Employee and Manager classes.
- Inheritance and method overriding.
- Custom exceptions and exception handling.
- List comprehensions, map, filter and lambda functions.

## Task 2 – Files, APIs and Environment

- Reading and writing CSV and JSON files.
- Extracting high-earning employees.
- REST API integration using requests.
- Handling API errors and timeouts.
- Environment variables using python-dotenv.
- Virtual environment and dependency management.

## Task 3 – NumPy, Pandas and Matplotlib

- NumPy arrays, broadcasting and weighted scores.
- Employee data exploration and cleaning.
- Missing salary values handled using median imputation.
- Duplicate record removal.
- Department-wise salary and headcount analysis.
- Inner, left and outer joins.
- Four salary visualisations using Matplotlib.

## Task 4 – Git, Terminal and Notebook

- Git feature branch workflow.
- Terminal commands and folder organisation.
- Jupyter Notebook with Markdown documentation.
- Performance measurement using %timeit.
- Notebook export using nbconvert.

## Project Structure

    week1-assessment/
    ├── data/
    │   ├── employees.csv
    │   ├── employees_missing.csv
    │   └── departments.csv
    ├── notebooks/
    │   ├── employee_analysis.ipynb
    │   └── employee_analysis.py
    ├── reports/
    │   └── charts/
    │       ├── department_salary_bar.png
    │       ├── salary_histogram.png
    │       ├── salary_scatter.png
    │       └── salary_line.png
    ├── src/
    │   ├── task1.py
    │   ├── task2.py
    │   └── task3_analysis.py
    ├── employees.json
    ├── high_earners.csv
    ├── users.json
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Requests
- Python-dotenv
- Jupyter Notebook
- Git and GitHub
- Visual Studio Code

## Setup Instructions

### 1. Clone the repository

    git clone -b feature/analysis https://github.com/manojkumaramtalawar-cmd/week1-assessment.git
    cd week1-assessment

### 2. Create a virtual environment

    python -m venv .venv

### 3. Activate the virtual environment on Windows

    .\.venv\Scripts\Activate.ps1

### 4. Install dependencies

    python -m pip install -r requirements.txt
    python -m pip install notebook ipykernel nbconvert

### 5. Configure environment variables

Create a local .env file containing an API_KEY variable. Do not commit this file to GitHub.

### 6. Run Python scripts

    python src/task1.py
    python src/task2.py
    python src/task3_analysis.py

### 7. Run Jupyter Notebook

    python -m jupyter notebook

Open notebooks/employee_analysis.ipynb and execute all cells.

### 8. Export the notebook

    python -m nbconvert --to script notebooks/employee_analysis.ipynb

## Key Findings

1. Five employees in the original dataset earn more than ₹50,000.
2. Chennai has four employees in the original dataset.
3. IT has the highest employee headcount in the original dataset.
4. Finance has the highest average salary in the original dataset.
5. Marketing is identified as a department without employees through the outer join.

## Limitations

- The dataset contains a small number of employees.
- Missing salary values are estimated using the median.
- Department heads and budgets are illustrative sample values.
- The findings should not be generalised to a larger organisation.

## Git Branch

All assessment development is maintained on the feature/analysis branch.

## Conclusion

This assessment demonstrates an end-to-end Python data analysis workflow, from data collection and cleaning to analysis, visualisation and version control.