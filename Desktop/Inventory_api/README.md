# Inventory Management API

This is an Inventory Management API built with Django and Django REST Framework (DRF) that allows users to manage inventory items, track inventory changes, and handle user authentication. The API is designed to simulate real-world inventory management for a store, providing essential CRUD operations, user management, and secure authentication.

---

## Features

- **User Management:**

  - Register, login, and manage users.
  - Token-based authentication using JWT.
  - Role-based access control.

- **Inventory Item Management:**

  - Create, read, update, and delete inventory items.
  - Track essential attributes like name, description, quantity, price, category, and timestamps.

- **Inventory Change Log:**

  - Log and track changes to inventory items (e.g., restocking or sales).
  - View the change history of inventory items.

- **Advanced Features:**

  - Pagination and sorting of inventory items.
  - Filters for categories, price range, and low stock.
  - Optional features like low-stock alerts, supplier management, and multi-store support.

- **Deployment-Ready:**
  - Deployed on Heroku or PythonAnywhere.
  - Secure and scalable.

---

## Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **Deployment:** Heroku or PythonAnywhere
- **Environment Variables Management:** `python-dotenv`

---

## Prerequisites

- Python 3.10+
- PostgreSQL database
- pip for managing dependencies

---

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/inventory-management-api.git
   cd inventory-management-api
   ```

## API Endpoints

## Inventory Management:

## 1. Create Inventory Item

Method: POST
path: api/inventory-items/
Request body: { "name":"Pineapple" , "quantity":"10", "price":"1000", "description":"Very fresh Pineapple", "category": "Fruits"}
Response body: 201 Created

## 2. Get All Inventory Items

Method: GET
path: api/inventory-items/
Response:
{
"count": 12,
"next": "http://127.0.0.1:8000/api/inventory-items/?page=2",
"previous": null,
"results": [
{
"id": 1,
"name": "tawab",
"description": null,
"quantity": 10,
"price": "3000.00",
"category": {
"id": 1,
"name": "Electronics",
"description": null,
"date_added": "2024-12-30T13:20:00.612076Z"
},
"date_added": "2024-12-30T13:20:11.198583Z",
"last_updated": "2024-12-30T13:20:11.198616Z"
},
{
"id": 2,
"name": "tawabprecious",
"description": null,
"quantity": 80,
"price": "60000.00",
"category": {
"id": 1,
"name": "Electronics",
"description": null,
"date_added": "2024-12-30T13:20:00.612076Z"
},
"date_added": "2024-12-30T13:33:10.300764Z",
"last_updated": "2024-12-30T14:03:48.634244Z"
},
{
"id": 3,
"name": "precious",
"description": null,
"quantity": 10,
"price": "4000.00",
"category": {
"id": 1,
"name": "Electronics",
"description": null,
"date_added": "2024-12-30T13:20:00.612076Z"
},
"date_added": "2024-12-30T13:54:24.985393Z",
"last_updated": "2024-12-30T13:54:24.985423Z"
},
{
"id": 4,
"name": "rosine",
"description": null,
"quantity": 103,
"price": "4000000.00",
"category": {
"id": 1,
"name": "Electronics",
"description": null,
"date_added": "2024-12-30T13:20:00.612076Z"
},
"date_added": "2024-12-30T14:14:42.272126Z",
"last_updated": "2024-12-30T14:14:42.272165Z"
},
{
"id": 5,
"name": "rice",
"description": null,
"quantity": 200,
"price": "900.00",
"category": {
"id": 1,
"name": "Electronics",
"description": null,
"date_added": "2024-12-30T13:20:00.612076Z"
},
"date_added": "2024-12-30T14:15:10.151217Z",
"last_updated": "2024-12-30T14:15:10.151254Z"
}
]
}

## 3. Update Inventory item

Method: PUT
Path:api/inventory-items/<int:pk>/
Request:
{
"name": "ricebeans"
"price": "500"
"description" : "combined rice and beans"
}
Response: 200 OK

User Authentication:

## 1. User Registration

Method: GET
Path: api/register/
Request Body: {
"username": "rosine"
"email": "rosine@gmail.com"
"password": "1234"
}
Response: 201 Creataed

## 2. Login

Method: POST
Path: api/login/
Request Body:
{
"username": "rosine"
"email": "rosine@gmail.com"
"password": "1234"
}
Response: 201 OK
