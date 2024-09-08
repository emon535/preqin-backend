from pydantic import BaseModel
from typing import Optional

class CommitmentBase(BaseModel):
    investor_id: int
    asset_class: str
    amount: float
    currency: str

class CommitmentCreate(CommitmentBase):
    pass

class CommitmentResponse(CommitmentBase):
    id: int

    class Config:
        orm_mode = True
