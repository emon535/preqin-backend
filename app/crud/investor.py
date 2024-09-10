from sqlalchemy.orm import Session
from typing import List, Optional, Tuple
from app.models import Investor, Commitment
from app import schemas
from app.schemas.commitment import CommitmentResponse


def get_commitments_and_total(db: Session, investor_id: int, asset_class: Optional[str] = None) -> Tuple[List[Commitment], float]:
    query = db.query(Commitment).filter(Commitment.investor_id == investor_id)
    
    if asset_class:
        query = query.filter(Commitment.asset_class == asset_class)

    commitments = query.all()
    total_commitments = sum(c.amount for c in commitments) if commitments else 0.0

    return commitments, total_commitments


def get_investors(db: Session, skip: int = 0, limit: int = 10) -> List[schemas.InvestorResponse]:
    investors = db.query(Investor).offset(skip).limit(limit).all()
    results = []
    for investor in investors:
        _, total_commitments = get_commitments_and_total(db, investor.id)
        
        investor_date_added_str = investor.investor_date_added.strftime('%Y-%m-%dT%H:%M:%S.%f') if investor.investor_date_added else None
        investor_last_updated_str = investor.investor_last_updated.strftime('%Y-%m-%dT%H:%M:%S.%f') if investor.investor_last_updated else None
        
        investor_response = schemas.InvestorResponse(
            id=investor.id,
            investor_name=investor.investor_name,
            investor_type=investor.investor_type,
            investor_date_added=investor_date_added_str,
            investor_last_updated=investor_last_updated_str,
            investor_country=investor.investor_country,
            total_commitments=total_commitments
        )
        results.append(investor_response)
    
    return results

def get_investors_by_id(db: Session, investor_id: int, asset_class: Optional[str] = None) -> schemas.InvestorDetailResponse:
    investor = db.query(Investor).filter(Investor.id == investor_id).first()
    if investor:
        commitments, total_commitments = get_commitments_and_total(db, investor_id, asset_class)
        
        return schemas.InvestorDetailResponse(
            **investor.__dict__,
            total_commitments=total_commitments,
            commitments=[CommitmentResponse.model_validate(c) for c in commitments]
        )    
    
    return None

def get_commitments_by_investor_id(db: Session, investor_id: int, asset_class: Optional[str] = None) -> List[Commitment]:
    query = db.query(Commitment).filter(Commitment.investor_id == investor_id)
    
    if asset_class:
        query = query.filter(Commitment.asset_class == asset_class)
    
    commitments = query.all()
    return commitments