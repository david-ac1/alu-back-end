#!/usr/bin/python3
"""
Script that uses a REST API to return information about
an employee's TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODOs
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Completed tasks
    completed_tasks = [t for t in todos_data if t.get("completed")]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Print header
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

    # Print each completed task exactly as required
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

