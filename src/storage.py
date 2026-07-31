import json
from pathlib import Path
from uuid import UUID

from src.models import Expense

DATA_FILE = Path("data/expenses.json")


def load_expenses() -> list[Expense]:
    """Load all expenses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Expense.model_validate(item) for item in data]


def save_expenses(expenses: list[Expense]) -> None:
    """Save all expenses to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            [expense.model_dump(mode="json") for expense in expenses],
            file,
            indent=4,
        )


def add_expense(expense: Expense) -> Expense:
    """Add a new expense."""
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    return expense


def delete_expense(expense_id: UUID) -> bool:
    """Delete an expense by ID."""
    expenses = load_expenses()

    filtered = [
        expense
        for expense in expenses
        if expense.id != expense_id
    ]

    if len(filtered) == len(expenses):
        return False

    save_expenses(filtered)
    return True