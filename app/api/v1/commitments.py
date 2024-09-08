from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import crud_commitments
from schemas import commitment_schemas
from db.database import get_db

router = APIRouter()

@router.get("/investors/{investor_id}/commitments", response_model=List[commitment_schemas.Commitment])
def get_commitments_by_investor(investor_id: int, db: Session = Depends(get_db)):
    commitments = crud_commitments.get_commitments_by_investor(db, investor_id=investor_id)
    if not commitments:
        raise HTTPException(status_code=404, detail="No commitments found for this investor")
    return commitments


@router.get("/commitments", response_model=List[commitment_schemas.Commitment])
def get_commitments_by_asset_class(asset_class: str, db: Session = Depends(get_db)):
    commitments = crud_commitments.get_commitments_by_asset_class(db, asset_class=asset_class)
    if not commitments:
        raise HTTPException(status_code=404, detail="No commitments found for the given asset class")
    return commitments


@router.post("/investors/{investor_id}/commitments", response_model=commitment_schemas.Commitment)
def create_commitment(investor_id: int, commitment: commitment_schemas.CommitmentCreate, db: Session = Depends(get_db)):
    return crud_commitments.create_commitment(db, investor_id=investor_id, commitment=commitment)
