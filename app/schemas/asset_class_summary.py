# app/schemas/asset_class.py

from pydantic import BaseModel
from typing import List

class AssetClassBase(BaseModel):
    name: str
    total_value: float

class AssetClassResponse(BaseModel):
    asset_classes: List[AssetClassBase]
