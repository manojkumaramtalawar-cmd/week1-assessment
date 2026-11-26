

import csv
import json
from pathlib import Path

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Define file paths
csv_file = BASE_DIR / "data" / "employees.csv"
json_file = BASE_DIR / "employees.json"
high_earners_file = BASE_DIR / "high_earners.csv"

# Read employees.csv using csv.DictReader
with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

print("Rows read:", len(employees))

# Convert salary from string to integer
for employee in employees:
    employee["salary"] = int(employee["salary"])


with open(json_file, "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

# Filter employees with salary above 50000
high_earners = [
    employee for employee in employees
    if employee["salary"] > 50000
]

# Write high_earners.csv
with open(high_earners_file, "w", newline="", encoding="utf-8") as file:
    fieldnames = ["id", "name", "department", "salary", "city"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(high_earners)

print("High earners:", len(high_earners))
print("employees.json created")
print("high_earners.csv created")

# API request using requests

import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("API_KEY")

# API URL
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)

    # Handle 404 error
    if response.status_code == 404:
        print("Error: API resource not found")

    else:
        response.raise_for_status()

        users = response.json()

        # Parse nested JSON using .get()
        user_data = []

        for user in users:
            user_info = {
                "id": user.get("id"),
                "name": user.get("name"),
                "username": user.get("username"),
                "email": user.get("email"),
                "city": user.get("address", {}).get("city"),
                "company": user.get("company", {}).get("name")
            }

            user_data.append(user_info)

        # Write users.json
        with open(BASE_DIR / "users.json", "w", encoding="utf-8") as file:
            json.dump(user_data, file, indent=4)

        print("Users fetched:", len(user_data))
        print("users.json created")

except requests.exceptions.Timeout:
    print("Error: API request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to API")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("API request error:", error)