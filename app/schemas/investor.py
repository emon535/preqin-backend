from pydantic import BaseModel
from typing import Optional

class InvestorBase(BaseModel):
    investor_name: str
    investor_type: str
    investor_country: str
    investor_date_added: Optional[str]
    investor_last_updated: Optional[str]

class InvestorCreate(InvestorBase):
    pass

class InvestorUpdate(InvestorBase):
    pass

class InvestorResponse(InvestorBase):
    total_commitments: float

class InvestorDetailResponse(InvestorBase):
    total_commitments: float
