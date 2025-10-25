#!/usr/bin/python3
"""
Script that uses a REST API to return information about
an employee’s TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list for the user
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get("name")

    # Filter completed tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Print progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    # Print each completed task title
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
