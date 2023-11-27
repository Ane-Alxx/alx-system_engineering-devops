#!/usr/bin/python3
"""solution for task 000"""

import requests
import sys


def get_employee_todo_progress(employee_id):
	""" Check if TODO data is cached """
	if employee_id not in cached_todos:
		""" Fetch TODO items """
		todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
		todos_data = todos_response.json()

		""" Cache TODO items """
		cached_todos[employee_id] = todos_data

	""" Fetch user information """
	user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
	user_data = user_response.json()
	employee_name = user_data.get('name')

	""" Calculate progress """
	total_tasks = 0
	completed_tasks = 0
	for task in cached_todos[employee_id]:
		if task.get('userId') == employee_id:
			total_tasks += 1
			if task.get('completed'):
				completed_tasks += 1

	""" Format and display output """
	progress_message = "Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks)
	print(progress_message)

	completed_tasks_list = []
	for task in cached_todos[employee_id]:
		if task.get('userId') == employee_id and task.get('completed'):
			completed_tasks_list.append("\t" + task.get('title'))

	for task in completed_tasks_list:
		print(task)

""" Initialize cached_todos dictionary """
cached_todos = {}

if __name__ == "__main__":
	employee_id = int(input("Enter employee ID: "))
	get_employee_todo_progress(employee_id)
