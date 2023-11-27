#!/usr/bin/python3
"""Solution for task 003"""

import json
import requests

def export_all_employees_data_to_json():
	# Fetch all users and their respective TODO items
	users_response = requests.get("https://jsonplaceholder.typicode.com/users")
	users_data = users_response.json()

	todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
	todos_data = todos_response.json()

	# Create and populate JSON data structure
	all_employees_data = {}

	for user in users_data:
		employee_id = user.get('id')
		username = user.get('username')
		task_list = []

		for task in todos_data:
			if task.get('userId') == employee_id:
				task_dict = {
					"username": username,
					"task": task.get('title'),
					"completed": task.get('completed')
				}
				task_list.append(task_dict)

		all_employees_data[str(employee_id)] = task_list

	# Create JSON file and write data
	filename = 'todo_all_employees.json'
	with open(filename, mode='w') as f:
		json.dump(all_employees_data, f, indent=4)

if __name__ == "__main__":
	export_all_employees_data_to_json()
