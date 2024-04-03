Todo App README

This README provides an overview of a Todo App built with Python FastAPI. The Todo App allows users to manage their tasks by providing four main routes:

Get Todos: Retrieve a list of all todos.
Create Todo: Add a new todo to the list.
Update Todo: Modify an existing todo.
Delete Todo: Remove a todo from the list.

Installation
1)Clone the Repository:
2) Install Dependencies: pip install -r requirements.txt

Usage
Run the Server:
Start the FastAPI server by executing the following command in the terminal:
uvicorn main:app --reload
The server will start running on http://localhost:8000 by default.

Access the API:
You can now access the Todo App API using tools like cURL, Postman, or by visiting /docs route.

Routes
1. Get Todos
Method: GET
URL: /todos
Description: Retrieve a list of all todos.

2. Create Todo
Method: POST
URL: /todos
Description: Add a new todo to the list.

3.  Update Todo
Method: PUT
URL: /todos/{todo}
Description: Modify an existing todo.

4. Delete Todo
Method: DELETE
URL: /todos/{todo_id}
Description: Remove a todo from the list.
