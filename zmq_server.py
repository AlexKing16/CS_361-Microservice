import time
from datetime import datetime
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5554")

def priority_sort(full_list):
    print("Sorting tasks by priority")

    tasks = full_list['tasks']

    # assign values to priorities for comparisons
    priority_values = {
        'High': 1,
        'Medium': 2,
        'Low': 3
    }
    sorted_tasks = []
    for task in tasks:
        if len(sorted_tasks) == 0:
            sorted_tasks.append(task)
        else:
            # sorts tasks based on priority
            for cur_task in sorted_tasks:
                if priority_values[task['priority']] < priority_values[cur_task['priority']]:
                    index = sorted_tasks.index(cur_task)
                    sorted_tasks.insert(index, task)
                    break
                # sorts tasks with same priority by due date
                elif priority_values[task['priority']] == priority_values[cur_task['priority']]:
                    if date_conversion(task['due_date']) < date_conversion(cur_task['due_date']):
                        index = sorted_tasks.index(cur_task)
                        sorted_tasks.insert(index, task)
                        break
            if task not in sorted_tasks:
                sorted_tasks.append(task)
    full_list['tasks'] = sorted_tasks

def duedate_sort(full_list):
    print("Sorting tasks by due date")

    tasks = full_list['tasks']

    # assign values to priorities for comparisons
    priority_values = {
        'High': 1,
        'Medium': 2,
        'Low': 3
    }
    sorted_tasks = []
    for task in tasks:
        if len(sorted_tasks) == 0:
            sorted_tasks.append(task)
        else:
            # sorts tasks based on due date
            for cur_task in sorted_tasks:
                if date_conversion(task['due_date']) < date_conversion(cur_task['due_date']):
                    index = sorted_tasks.index(cur_task)
                    sorted_tasks.insert(index, task)
                    break
                # sort tasks with same due dates by priority
                elif date_conversion(task['due_date']) == date_conversion(cur_task['due_date']):
                    if priority_values[task['priority']] < priority_values[cur_task['priority']]:
                        index = sorted_tasks.index(cur_task)
                        sorted_tasks.insert(index, task)
                        break
            if task not in sorted_tasks:
                sorted_tasks.append(task)
    full_list['tasks'] = sorted_tasks

def date_conversion(date_str):
    """
    Converts date string from JSON to datetime for accurate time comparisons
    :param date_str: date string
    :return: datetime object
    """
    converted_date = datetime.strptime(date_str, "%Y-%m-%d")
    return converted_date

def sort(to_sort):
    print('Sort type:', to_sort['sort_type'])
    sort_condition = to_sort['sort_type'].lower()

    if sort_condition == 'priority':
        priority_sort(to_sort)
    elif sort_condition == 'due date':
        duedate_sort(to_sort)
    else:
        return "ERROR"

while True:
    #  Wait for request from client
    print('Listening for requests...')
    task_list = socket.recv_json()
    print("Received request")

    #  Sort received request based on type of sort indicated
    time.sleep(1)
    sort_request = sort(task_list)

    #  Send reply back to client
    if sort_request == "ERROR":
        socket.send_json({"Error": "Sort type not found"})
    else:
        print('Sending sorted task list back to client')
        print('')
        socket.send_json(task_list)
