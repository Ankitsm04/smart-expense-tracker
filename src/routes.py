from uuid import UUID

from fastapi import APIRouter, HTTPException, Query

from src.models import Expense, ExpenseCreate, ExpenseSummary
from src.storage import add_expense, delete_expense, load_expenses

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("", response_model=Expense, status_code=201)
def create_expense(expense: ExpenseCreate):
    new_expense = Expense(**expense.model_dump())
    return add_expense(new_expense)


@router.get("", response_model=list[Expense])
def get_expenses(category: str | None = Query(default=None)):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense.category.lower() == category.lower()
        ]

    return expenses


@router.get("/total", response_model=ExpenseSummary)
def get_total(category: str | None = Query(default=None)):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense.category.lower() == category.lower()
        ]

    total = sum(expense.amount for expense in expenses)

    return ExpenseSummary(total=total)


@router.delete("/{expense_id}")
def remove_expense(expense_id: UUID):
    deleted = delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    return {"message": "Expense deleted successfully"}