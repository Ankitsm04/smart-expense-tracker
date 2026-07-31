from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from src.main import app
import src.storage as storage

client = TestClient(app)


@pytest.fixture(autouse=True)
def temp_storage(tmp_path, monkeypatch):
    """
    Use a temporary JSON file for every test.
    """
    temp_file = tmp_path / "expenses.json"
    temp_file.write_text("[]")

    monkeypatch.setattr(storage, "DATA_FILE", temp_file)

    yield


def test_create_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Lunch"
    assert data["amount"] == 250
    assert data["category"] == "Food"
    assert "id" in data


def test_get_all_expenses():
    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_by_category():
    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Uber",
            "amount": 300,
            "category": "Travel",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses?category=Food")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["category"] == "Food"


def test_total_expenses():
    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Uber",
            "amount": 300,
            "category": "Travel",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 550


def test_total_by_category():
    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 500,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses/total?category=Food")

    assert response.status_code == 200
    assert response.json()["total"] == 750


def test_delete_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    expense_id = response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")

    assert delete_response.status_code == 200

    all_expenses = client.get("/expenses")

    assert len(all_expenses.json()) == 0


def test_delete_non_existing():
    response = client.delete(
        "/expenses/11111111-1111-1111-1111-111111111111"
    )

    assert response.status_code == 404


def test_invalid_amount():
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": -10,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 422


def test_missing_field():
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 422