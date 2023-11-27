#!/usr/bin/python3
"""Solution for task 002"""

import json
import requests

def export_employee_data_to_json(employee_id):
	""" Fetch user information """
	user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
	user_data = user_response.json()
	username = user_data.get('username')

	""" Fetch TODO items for the specified employee """
	todos_response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
	todos_data = todos_response.json()

	""" Create and populate JSON data structure """
	employee_data = {}
	task_list = []

	for task in todos_data:
		task_dict = {
			"task": task.get('title'),
			"completed": task.get('completed'),
			"username": username
		}
		task_list.append(task_dict)

	employee_data[str(employee_id)] = task_list

	""" Create JSON file named after the user ID and write data """
	filename = str(employee_id) + '.json'
	with open(filename, mode='w') as f:
		json.dump(employee_data, f, indent=4)

if __name__ == "__main__":
	employee_id = int(input("Enter employee ID: "))
	export_employee_data_to_json(employee_id)
