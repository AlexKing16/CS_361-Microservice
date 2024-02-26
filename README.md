# CS_361-Microservice

Requesting Data
1) Make sure the server is running and that your code is set up to establish a connection to the server.
2) Use the send_json function to send a properly formatted JSON object to the server for sorting.
Example
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5554")
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
socket.send_json(task_list)

Receiving Data
1) After sending the JSON object to the server, it will sort the tasks based on the indicated sort type, and send back the JSON object with the tasks sorted in the correct order.
2) Set up a variable to receive and contain the content of the recv_json function.
3) This variable will now contain the JSON object with the tasks sorted in the correct order, and can be used in your code.

Example - in conjunction with the above example

sorted_task_list = socket.recv_json()
print(f"Organized task list: {sorted_task_list}")
--> Organized task list: {'sort_type': 'priority', 'tasks': [{'title': 'Another high priority', 'priority': 'High', 'due_date': '2024-02-19'}, {'title': 'Complete project proposal', 'priority': 'High', 'due_date': '2024-02-20'}, {'title': 'Buy groceries', 'priority': 'Medium', 'due_date': '2024-02-15'}, {'title': 'Finish coding assignment', 'priority': 'Low', 'due_date': '2024-02-25'}]}



<img width="1085" alt="Screenshot 2024-02-26 at 2 38 32 PM" src="https://github.com/AlexKing16/CS_361-Microservice/assets/55066365/5d02fdb4-edbd-4969-bbee-d8eaa1b32b86">


