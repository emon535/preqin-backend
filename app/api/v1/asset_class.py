
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.asset_class_summary import AssetClassResponse
from app.db.database import get_db
from app.crud.asset_class import get_asset_class_totals

router = APIRouter()

@router.get("/", response_model=AssetClassResponse)
def read_asset_classes(db: Session = Depends(get_db)):
    asset_class_totals = get_asset_class_totals(db)
    return AssetClassResponse(
        asset_classes=asset_class_totals
    )