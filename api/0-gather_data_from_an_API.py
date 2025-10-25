#!/usr/bin/python3
"""
Script that uses a REST API to return information about
an employee's TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        sys.exit(1)
    todos_data = todos_response.json()

    # Filter completed tasks (exact boolean check)
    completed_tasks = [task for task in todos_data if task.get("completed") is True]

    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Print header line exactly
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

    # Print completed tasks exactly as required (\t + space before title)
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
