from sqlalchemy.orm import Session
from .. import models, schemas

def create_commitment(db: Session, commitment: schemas.CommitmentCreate) -> models.Commitment:
    db_commitment = models.Commitment(
        investor_id=commitment.investor_id,
        asset_class=commitment.asset_class,
        amount=commitment.amount,
        currency=commitment.currency
    )
    db.add(db_commitment)
    db.commit()
    db.refresh(db_commitment)
    return db_commitment
