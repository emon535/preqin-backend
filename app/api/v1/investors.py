from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas import InvestorResponse, InvestorDetailResponse, CommitmentResponse
from app.db.database import get_db
from app.crud.investor import get_investors, get_investors_by_id, get_commitments_by_investor_id

router = APIRouter()

@router.get("/", response_model=List[InvestorResponse])
def read_investors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_investors(db, skip=skip, limit=limit)

@router.get("/{investor_id}", response_model=InvestorDetailResponse)
def read_investor_by_id(investor_id: int, asset_class: Optional[str] = None, db: Session = Depends(get_db)):
    investor = get_investors_by_id(db, investor_id)
    if investor is None:
        raise HTTPException(status_code=404, detail="Investor not found")
    

    commitments = get_commitments_by_investor_id(db, investor_id, asset_class)
    total_commitments = sum(c.amount for c in commitments)


    return InvestorDetailResponse(
        id=investor.id,
        investor_name=investor.investor_name,
        investor_type=investor.investor_type,
        investor_date_added=investor.investor_date_added.strftime('%Y-%m-%dT%H:%M:%S.%f') if investor.investor_date_added else None,
        investor_last_updated=investor.investor_last_updated.strftime('%Y-%m-%dT%H:%M:%S.%f') if investor.investor_last_updated else None,
        investor_country=investor.investor_country,
        total_commitments=total_commitments,
        commitments=[CommitmentResponse.model_validate(c) for c in commitments]
    )


