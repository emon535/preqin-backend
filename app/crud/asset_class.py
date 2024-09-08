from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas

def get_asset_classes(db: Session) -> List[models.AssetClass]:
    return db.query(models.AssetClass).all()

def create_asset_class(db: Session, asset_class: schemas.AssetClassCreate) -> models.AssetClass:
    db_asset_class = models.AssetClass(name=asset_class.name)
    db.add(db_asset_class)
    db.commit()
    db.refresh(db_asset_class)
    return db_asset_class
