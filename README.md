# 🚀 RESTful FastAPI  

## A blazing-fast RESTful API built with FastAPI

This API provides **quick and efficient CRUD operations** for managing items in a database. Whether you're building a microservice or learning about RESTful APIs, this project is a perfect starting point. Star the project if you find it useful.

## Why FASTAPI?

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3

Python's flask RESTful APIs are not as fast, especially when using the APi at larger scales

---

## 🔹 Features

✅ **Create** an item in the database.  
✅ **Retrieve** a single item or multiple items.  
✅ **Update** an existing item.  
✅ **Delete** an item from the database.  

Built using **FastAPI**, this project leverages **asynchronous execution** for high performance while maintaining a clean and intuitive API structure.  

---

## 📌 Understanding RESTful API

An **API (Application Programming Interface)** is a set of **rules and protocols** that allow software applications to communicate.  

A **RESTful API (Representational State Transfer API)** follows the **REST principles**, which are defined by:  

- 🔹 Using **HTTP methods** (`GET`, `POST`, `PUT`, `DELETE`).  
- 🔹 Maintaining **stateless communication** (no session tracking).  
- 🔹 Returning **data in JSON or XML format**.  
- 🔹 Using **resource-based endpoints**, e.g., `/items/{item_id}`.  

---

## 🛠 Installation Instructions  

Follow these steps to set up and run the API locally:  

1. Clone the repository using `git clone 'https://github.com/your-username/restful-fast''

2. cd into the project directory.

3. Run the following command in your terminal: uvicorn main:app --reload

4. Open a web browser and navigate to 'http://127.0.0.1:8000/'

5. You can use POSTMAN or CURL to test the endpoint

- Get an item from the database

"curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "name": "Laptop",
  "price": 999.99,
  "quantity": 10
}'"

- Get all items from the database

"curl -X 'GET' 'http://127.0.0.1:8000/items/'"

- Get a specific item from the database

"curl -X 'GET' 'http://127.0.0.1:8000/items/1'"

- Update an item in the database

"curl -X 'PUT' \
  'http://127.0.0.1:8000/items/1' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "name": "Gaming Laptop",
  "price": 1299.99,
  "quantity": 5
}'"

- Delete an item from the database

"curl -X 'DELETE' 'http://127.0.0.1:8000/items/1'"

- Deploying Your FastAPI App
You can deploy your API using Docker, Heroku, or AWS Lambda.

Quickest Way is to deploy on Render
Push your code to GitHub.
Go to Render and create a new web service.
Select Python and point it to your repository.
Set the start command:
uvicorn main:app --host 0.0.0.0 --port $PORT
Deploy! 🚀

This project is freely licensed under the MIT License. Feel free to use it for your own projects. If you have any questions reach out to me.
