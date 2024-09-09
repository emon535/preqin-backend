from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from app.models import Investor, Commitment
from app import schemas
from app.schemas.commitment import CommitmentResponse

def get_investors(db: Session, skip: int = 0, limit: int = 10) -> List[schemas.InvestorResponse]:
    investors = db.query(Investor).offset(skip).limit(limit).all()
    results = []
    for investor in investors:
        total_commitments = db.query(func.sum(Commitment.amount)).filter(Commitment.investor_id == investor.id).scalar() or 0
       
        investor_date_added_str = investor.investor_date_added.strftime('%Y-%m-%dT%H:%M:%S.%f') if investor.investor_date_added else None
        investor_last_updated_str = investor.investor_last_updated.strftime('%Y-%m-%dT%H:%M:%S.%f') if investor.investor_last_updated else None
        
        investor_response = schemas.InvestorResponse(
            id=investor.id,
            investor_name=investor.investor_name,
            investor_type=investor.investor_type,
            investor_date_added= investor_date_added_str,
            investor_last_updated = investor_last_updated_str,
            investor_country=investor.investor_country,
            total_commitments=total_commitments
        )
        results.append(investor_response)
    
    return results

def get_investors_by_id(db: Session, investor_id: int) -> schemas.InvestorDetailResponse:
    investor = db.query(Investor).filter(Investor.id == investor_id).first()
    if investor:
        total_commitments = db.query(func.sum(Commitment.amount)).filter(Commitment.investor_id == investor.id).scalar() or 0
        commitments = get_commitments_by_investor_id(db, investor_id)
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
    
    print(f"Number of commitments for investor_id {investor_id} with asset_class {asset_class}: {len(commitments)}")
    for commitment in commitments:
        print(f"Commitment ID: {commitment.id}, Investor ID: {commitment.investor_id}, Amount: {commitment.amount}, Asset Class: {commitment.asset_class}")
    
    return commitments