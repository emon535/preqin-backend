
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class InvestorBase(BaseModel):
    investor_name: str
    investor_type: Optional[str] = None
    investor_country: Optional[str] = None

class InvestorCreate(InvestorBase):
    pass

class InvestorResponse(InvestorBase):
    id: int
    investor_date_added: date
    investor_last_updated: date

    class Config:
        orm_mode = True
