from sqlalchemy.orm import Session
from typing import List
import models
import schemas


def get_investors(db: Session, skip: int = 0, limit: int = 10) -> List[models.Investor]:
    return db.query(models.Investor).offset(skip).limit(limit).all()

def get_investor_by_id(db: Session, investor_id: int) -> models.Investor:
    return db.query(models.Investor).filter(models.Investor.id == investor_id).first()

def create_investor(db: Session, investor: schemas.InvestorCreate) -> models.Investor:
    db_investor = models.Investor(
        investor_name=investor.investor_name,
        investor_type=investor.investor_type,
        investor_country=investor.investor_country,
        investor_date_added=investor.investor_date_added,
        investor_last_updated=investor.investor_last_updated
    )
    db.add(db_investor)
    db.commit()
    db.refresh(db_investor)
    return db_investor
