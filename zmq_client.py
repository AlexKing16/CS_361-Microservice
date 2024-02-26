import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to task list organizer server…")
print('Connection successful')
print('')
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5554")

#  Task lists to send to server
task_list = {
  "sort_type": "priority",
  "tasks": [
    {
      "title": "Complete project proposal",
      "priority": "High",
      "due_date": "2024-02-20"
    },
    {
      "title": "Buy groceries",
      "priority": "Medium",
      "due_date": "2024-02-15"
    },
    {
      "title": "Finish coding assignment",
      "priority": "Low",
      "due_date": "2024-02-25"
    },
    {
      "title": "Another high priority",
      "priority": "High",
      "due_date": "2024-02-19"
    }
  ]
}
task_list2 = {
  "sort_type": "due date",
  "tasks": [
    {
      "title": "Complete project proposal",
      "priority": "High",
      "due_date": "2024-02-20"
    },
    {
      "title": "Buy groceries",
      "priority": "Medium",
      "due_date": "2024-02-15"
    },
    {
      "title": "Finish coding assignment",
      "priority": "Low",
      "due_date": "2024-02-25"
    },
    {
      "title": "Another high priority",
      "priority": "High",
      "due_date": "2024-02-19"
    }
  ]
}
task_list3 = {
  "sort_type": "time",
  "tasks": [
    {
      "title": "Complete project proposal",
      "priority": "High",
      "due_date": "2024-02-20"
    },
    {
      "title": "Buy groceries",
      "priority": "Medium",
      "due_date": "2024-02-15"
    },
    {
      "title": "Finish coding assignment",
      "priority": "Low",
      "due_date": "2024-02-25"
    }
  ]
}
tests = [task_list, task_list2, task_list3]

for lists in tests:
  #  Send task lists to server
  print("Sending task list to server")
  socket.send_json(lists)

  #  Receive reply from server
  sorted_task_list = socket.recv_json()
  print(f"Organized task list: {sorted_task_list}")
  print('')
