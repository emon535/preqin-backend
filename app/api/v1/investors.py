from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import InvestorCreate, InvestorDetailResponse
from app.db.database import get_db
from app.crud.investor import get_investors, get_investors_by_id


router = APIRouter()

@router.get("/", response_model=List[InvestorDetailResponse])
def read_investors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    print("read_in")
    return get_investors(db, skip=skip, limit=limit)

@router.get("/{investor_id}", response_model= InvestorDetailResponse)
def read_investor_byId(investor_id: int, db: Session = Depends(get_db)):
    investor = get_investors_by_id(db, investor_id)
    if investor is None:
        raise HTTPException(status_code=404, detail="Investor not found")
    return investor

# @router.post("/", response_model=schemas.InvestorResponse)
# def create_investor(investor: schemas.InvestorCreate, db: Session = Depends(get_db)):
#     return crud.create_investor(db, investor)
