
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Commitment
from app.schemas import AssetClassBase

def get_asset_class_totals(db: Session):
    results = db.query(
        Commitment.asset_class,
        func.sum(Commitment.amount).label('total_value')
    ).group_by(Commitment.asset_class).all()


    asset_class_totals = [
        AssetClassBase(
            name=asset_class,
            total_value=total_value
        )
        for asset_class, total_value in results
    ]

    return asset_class_totals
