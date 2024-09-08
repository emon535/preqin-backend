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
        results.append(schemas.InvestorResponse(**investor.__dict__, total_commitments=total_commitments))
    return results

# def get_investor_by_id(db: Session, investor_id: int) -> schemas.InvestorDetailResponse:
#     investor = db.query(models.Investor).filter(models.Investor.id == investor_id).first()
#     if investor:
#         total_commitments = db.query(func.sum(models.Commitment.amount)).filter(models.Commitment.investor_id == investor.id).scalar() or 0
#         commitments = db.query(models.Commitment).filter(models.Commitment.investor_id == investor_id).all()
#         return schemas.InvestorDetailResponse(**investor.__dict__, total_commitments=total_commitments, commitments=[schemas.CommitmentResponse.from_orm(c) for c in commitments])
#     return None

def create_investor(db: Session, investor: schemas.InvestorCreate) -> Investor:
    db_investor = Investor(**investor.dict())
    db.add(db_investor)
    db.commit()
    db.refresh(db_investor)
    return db_investor
