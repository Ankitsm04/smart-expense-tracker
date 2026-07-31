# Smart Expense Tracker API

## Overview

Smart Expense Tracker API is a RESTful web service built with **FastAPI** that allows users to manage personal expenses. It supports creating, viewing, filtering, calculating totals, and deleting expenses. Data is stored in a local JSON file, so no database setup is required.

## Features

* Add a new expense
* View all expenses
* Filter expenses by category
* Calculate total expenses
* Calculate total expenses by category
* Delete an expense
* Interactive API documentation with Swagger UI
* Automated test suite using pytest

## Tech Stack

* Python 3.12+
* FastAPI
* Pydantic
* Uvicorn
* Pytest
* Local JSON file storage

## Project Structure

```text
smart-expense-tracker/
│
├── README.md
├── AI_NOTES.md
├── pyproject.toml
├── data/
│   └── expenses.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── storage.py
└── tests/
    └── test_api.py
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd smart-expense-tracker
```

## Prerequisites

Before running the project, ensure you have the following installed:

* Python 3.12 or later
* `pip` (comes with most Python installations)
* `uv`

Install `uv`:

```bash
pip install uv
```

## Install Dependencies

From the project root, run:

```bash
uv sync
```

## Run the Server

Start the development server:

```bash
uv run uvicorn src.main:app --reload
```

The API will be available at:

* API: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## Running the Tests

Execute the automated test suite:

```bash
uv run python -m pytest
```

## API Endpoints

| Method | Endpoint                              | Description                             |
| ------ | ------------------------------------- | --------------------------------------- |
| GET    | `/`                                   | Health check                            |
| POST   | `/expenses`                           | Add a new expense                       |
| GET    | `/expenses`                           | View all expenses                       |
| GET    | `/expenses?category={category}`       | Filter expenses by category             |
| GET    | `/expenses/total`                     | Calculate total expenses                |
| GET    | `/expenses/total?category={category}` | Calculate total expenses for a category |
| DELETE | `/expenses/{expense_id}`              | Delete an expense                       |

## Example Request

### Create Expense

**POST** `/expenses`

```json
{
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "date": "2026-07-31"
}
```

## Data Storage

Expenses are stored in:

```text
data/expenses.json
```

No external database is required.

## Validation

The API validates incoming requests using Pydantic.

Examples of invalid requests include:

* Negative expense amount
* Missing required fields
* Empty title or category
* Invalid date format

Invalid requests return **HTTP 422 Unprocessable Entity**.

## Design Decisions

* FastAPI for high-performance REST APIs
* Pydantic for request validation
* JSON file storage to satisfy the assignment requirement without a database
* Separation of concerns by keeping models, routes, and storage logic in separate modules
* Automated tests to verify API behavior

## Future Improvements

* Authentication and user accounts
* Persistent database support (SQLite/PostgreSQL)
* Update expense endpoint
* Pagination for large datasets
* Expense analytics and charts
* Search functionality
* Docker support
