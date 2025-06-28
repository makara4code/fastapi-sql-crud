# FastAPI SQL CRUD

A FastAPI-based REST API with SQLAlchemy ORM for managing products and users with multiple API versioning strategies.

## Features

- **CRUD Operations**: Full Create, Read, Update, Delete operations for Products and Users
- **SQLAlchemy Integration**: SQLite database with ORM
- **Pydantic Validation**: Request/response validation with Pydantic models
- **Multiple API Versioning Strategies**: Support for different versioning approaches
- **Authentication**: User authentication system
- **Error Handling**: Comprehensive HTTP error handling

## Project Structure

```
fastapi-sql-crud/
├── api/
│   ├── main.py
│   └── routes/
│       ├── v1/
│       │   ├── products.py
│       │   └── users.py
│       └── v2/
│           ├── products.py
│           └── users.py
├── routers/
│   ├── auth.py
│   ├── products.py
│   ├── routes.py
│   └── users.py
├── database.py
├── models.py
├── main.py
└── pyproject.toml
```

## API Versioning Strategies

This project supports multiple API versioning approaches:

### Option 1: Path Parameter Versioning
```
GET /v1/products
GET /v2/products
POST /v1/products
POST /v2/products
```

### Option 2: Query Parameter Versioning
```
GET /products?version=1
GET /products?version=2
POST /products?version=1
POST /products?version=2
```

### Option 3: Header-Based Versioning
```
GET /products
Headers: {"version": "1"}

GET /products  
Headers: {"version": "2"}
```

### Option 4: Subdomain-Based Versioning
```
v1.products.example.com/products
v2.products.example.com/products
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-sql-crud
```

2. Install dependencies:
```bash
pip install -e .
```

## Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Database Models

### Product
- `id`: Primary key
- `name`: Product name (max 100 characters)
- `price`: Product price (integer)
- `rating`: Product rating (1-5)

### User
- `id`: Primary key
- `name`: User name
- `age`: User age

## API Endpoints

### Products

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products/` | Get all products |
| GET | `/products/{product_id}` | Get product by ID |
| POST | `/products/` | Create new product |
| PUT | `/products/{product_id}` | Update product (full) |
| PATCH | `/products/{product_id}` | Update product (partial) |
| DELETE | `/products/{product_id}` | Delete product |

### Users

Similar CRUD operations available for users.

## Example Usage

### Create a Product
```bash
curl -X POST "http://localhost:8000/products/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sample Product",
    "price": 2999,
    "rating": 4
  }'
```

### Get All Products
```bash
curl -X GET "http://localhost:8000/products/"
```

### Get Product by ID
```bash
curl -X GET "http://localhost:8000/products/1"
```

## Requirements

- Python 3.12+
- FastAPI
- SQLAlchemy
- SQLite (default database)

## Development

The project uses:
- **FastAPI** for the web framework
- **SQLAlchemy** for database ORM
- **Pydantic** for data validation
- **SQLite** as the database (can be easily changed to PostgreSQL, MySQL, etc.)
