# app/schemas/commitment.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class CommitmentBase(BaseModel):
    commitment_name: str
    commitment_amount: float
    commitment_date: date

class CommitmentCreate(CommitmentBase):
    pass

class CommitmentResponse(CommitmentBase):
    id: int

    class Config:
        orm_mode = True
