from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import crud
from app.schemas.commitment import CommitmentCreate, CommitmentResponse

router = APIRouter()

@router.get("/test")
def get_commitments(db: Session = Depends(get_db)):
    return {"message": "This is a test endpoint"}

@router.post("/", response_model=CommitmentResponse)
def create_commitment(commitment: CommitmentCreate, db: Session = Depends(get_db)):
    return crud.create_commitment(db, commitment)
