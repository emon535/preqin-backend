from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import investor as crud_investors
from schemas import investor_schemas
from db.database import get_db

router = APIRouter()

@router.get("/investors", response_model=List[investor_schemas.Investor])
def get_investors(db: Session = Depends(get_db)):
    investors = crud_investors.get_investors(db)
    return investors

@router.get("/investors/{investor_id}", response_model=investor_schemas.Investor)
def get_investor_by_id(investor_id: int, db: Session = Depends(get_db)):
    investor = crud_investors.get_investor_by_id(db, investor_id=investor_id)
    if not investor:
        raise HTTPException(status_code=404, detail="Investor not found")
    return investor

@router.post("/investors", response_model=investor_schemas.Investor)
def create_investor(investor: investor_schemas.InvestorCreate, db: Session = Depends(get_db)):
    return crud_investors.create_investor(db, investor=investor)
