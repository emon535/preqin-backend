from pydantic import BaseModel

class CommitmentBase(BaseModel):
    asset_class: str
    amount: float
    currency: str

class CommitmentCreate(CommitmentBase):
    investor_id: int

# Response schema for Commitments
class CommitmentResponse(CommitmentBase):
    id: int

    class Config:
        orm_mode = True
