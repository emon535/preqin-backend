# app/api/commitment.py or app/routers/commitment.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import crud
from app.schemas.commitment import CommitmentCreate, CommitmentResponse
from app.crud.commitment import get_commitments_by_investor_id  # Adjust to the correct path

router = APIRouter()

@router.get("/test")
def get_commitments(db: Session = Depends(get_db)):
    return {"message": "This is a test endpoint"}

@router.get("/{investor_id}", response_model=list[CommitmentResponse])
def get_commitments_by_investorid(investor_id: int, db: Session = Depends(get_db)):
    return get_commitments_by_investor_id(db, investor_id)
