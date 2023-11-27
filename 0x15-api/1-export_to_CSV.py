#!/usr/bin/python3
"""Solution for task 001"""
import csv
import requests

def export_employee_data_to_csv(employee_id):
	""" Fetch user information """
	user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
	user_data = user_response.json()
	username = user_data.get('username')

	""" Fetch TODO items for the specified employee """
	todos_response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
	todos_data = todos_response.json()

	""" Create CSV file named after the user ID and write data """
	filename = str(employee_id) + '.csv'
	with open(filename, mode='w') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
		for task in todos_data:
			writer.writerow([employee_id, username, str(task.get('completed')), task.get('title')])

if __name__ == "__main__":
	employee_id = int(input("Enter employee ID: "))
	export_employee_data_to_csv(employee_id)
