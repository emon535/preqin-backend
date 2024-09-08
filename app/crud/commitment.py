from typing import List
from sqlalchemy.orm import Session
from app import models, schemas

def create_commitment(db: Session, commitment: schemas.CommitmentCreate) -> models.Commitment:
    db_commitment = models.Commitment(**commitment.dict())
    db.add(db_commitment)
    db.commit()
    db.refresh(db_commitment)
    return db_commitment



def get_commitments_by_investor_id(db: Session, investor_id: int, asset_class: str = None) -> List[schemas.CommitmentResponse]:
    query = db.query(models.Commitment).filter(models.Commitment.investor_id == investor_id)
    if asset_class:
        query = query.filter(models.Commitment.asset_class == asset_class)
    commitments = query.all()
    return [schemas.CommitmentResponse(**commitment.__dict__) for commitment in commitments]

def get_commitments_by_investor_id(db: Session, investor_id: int, asset_class: str = None) -> List[schemas.CommitmentResponse]:
    query = db.query(models.Commitment).filter(models.Commitment.investor_id == investor_id)
    if asset_class:
        query = query.filter(models.Commitment.asset_class == asset_class)
    commitments = query.all()
    return [schemas.CommitmentResponse(**commitment.__dict__) for commitment in commitments]
