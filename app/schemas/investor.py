from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from app.schemas.commitment import CommitmentResponse

# Base schema for Investor
class InvestorBase(BaseModel):
    investor_name: str
    investor_type: str
    investor_country: str

class InvestorCreate(InvestorBase):
    pass

# Response schema for Investor (with total commitments)
class InvestorResponse(InvestorBase):
    id: int
    total_commitments: float

    class Config:
        from_attributes = True 

# Detailed Response schema for Investor with Commitments
class InvestorDetailResponse(InvestorBase):
    id: int
    investor_name: str
    investor_type: str
    investor_country: str
    investor_date_added: datetime
    investor_last_updated: datetime
    total_commitments: float
    commitments: List[CommitmentResponse]  # Nested commitments

    class Config:
        from_attributes = True 
