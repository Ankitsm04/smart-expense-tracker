from datetime import date
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ConfigDict


class ExpenseCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=50)
    date: date


class Expense(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    amount: float
    category: str
    date: date

    model_config = ConfigDict(from_attributes=True)


class ExpenseSummary(BaseModel):
    total: float