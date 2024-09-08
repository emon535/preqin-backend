from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from app.models import Commitment
from schemas.asset_class_summary import AssetClassSummary

def get_asset_class_totals(db: Session) -> List[AssetClassSummary]:
    # Query to get asset class names and their total asset values
    results = db.query(
        Commitment.asset_class,
        func.sum(Commitment.amount).label('total_value')
    ).group_by(Commitment.asset_class).all()

    # Convert results to list of AssetClassSummary
    asset_class_summaries = [
        AssetClassSummary(
            asset_class=asset_class,
            total_value=total_value
        )
        for asset_class, total_value in results
    ]

    return asset_class_summaries