from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas import InvestorResponse, InvestorDetailResponse
from app.db.database import get_db
from app.crud.investor import get_investors, get_investors_by_id

router = APIRouter()

@router.get("/", response_model=List[InvestorResponse])
def read_investors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_investors(db, skip=skip, limit=limit)

@router.get("/{investor_id}", response_model=InvestorDetailResponse)
def read_investor_by_id(investor_id: int, asset_class: Optional[str] = None, db: Session = Depends(get_db)):
    investor = get_investors_by_id(db, investor_id, asset_class)
    if investor is None:
        raise HTTPException(status_code=404, detail="Investor not found")
    
    return investor

