from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from app.models import Investor, Commitment
from app import schemas

def get_investors(db: Session, skip: int = 0, limit: int = 10) -> List[schemas.InvestorResponse]:
    investors = db.query(Investor).offset(skip).limit(limit).all()
    results = []
    for investor in investors:
        total_commitments = db.query(func.sum(Commitment.amount)).filter(Commitment.investor_id == investor.id).scalar() or 0
        # Convert datetime to string
        investor_date_added_str = investor.investor_date_added.strftime('%Y-%m-%dT%H:%M:%S.%f') if investor.investor_date_added else None
        investor_last_updated_str = investor.investor_last_updated.strftime('%Y-%m-%dT%H:%M:%S.%f') if investor.investor_last_updated else None
        
        # Create InvestorResponse with datetime as string
        investor_response = schemas.InvestorDetailResponse(
            id=investor.id,
            investor_name=investor.investor_name,
            investor_type=investor.investor_type,
            investor_country=investor.investor_country,
            investor_date_added=investor_date_added_str,
            investor_last_updated=investor_last_updated_str,
            total_commitments=total_commitments
        )
        results.append(investor_response)
    
    print("Results:", results)  # Debugging line
    return results

def get_investors_by_id(db: Session, investor_id: int) -> schemas.InvestorDetailResponse:
    investor = db.query(Investor).filter(Investor.id == investor_id).first()
    if investor:
        total_commitments = db.query(func.sum(Commitment.amount)).filter(Commitment.investor_id == investor.id).scalar() or 0
        commitments = db.query(Commitment).filter(Commitment.investor_id == investor_id).all()
        print("Commitments:", commitments.append)
        return schemas.InvestorDetailResponse(**investor.__dict__, total_commitments=total_commitments, commitments=[schemas.CommitmentResponse.from_orm(c) for c in commitments])
    return None

# def create_investor(db: Session, investor: schemas.InvestorCreate) -> Investor:
#     db_investor = Investor(**investor.dict())
#     db.add(db_investor)
#     db.commit()
#     db.refresh(db_investor)
#     return db_investor
