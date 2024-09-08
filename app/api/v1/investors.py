from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

# @router.get("/", response_model=List[schemas.InvestorResponse])
# def read_investors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     print("read_in")
#     # return {"test": "test"}
#     return get_investors(db, skip=skip, limit=limit)

# @router.get("/{investor_id}", response_model=schemas.InvestorDetailResponse)
# def read_investor(investor_id: int, db: Session = Depends(get_db)):
#     investor = crud.get_investor_by_id(db, investor_id)
#     if investor is None:
#         raise HTTPException(status_code=404, detail="Investor not found")
#     return investor

# @router.post("/", response_model=schemas.InvestorResponse)
# def create_investor(investor: schemas.InvestorCreate, db: Session = Depends(get_db)):
#     return crud.create_investor(db, investor)
