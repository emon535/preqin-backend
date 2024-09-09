from fastapi import APIRouter


from . import investors  
from . import asset_class

api_router = APIRouter()

api_router.include_router(investors.router, prefix="/investors", tags=["investors"])
api_router.include_router(asset_class.router, prefix="/asset-class", tags=["asset-class"])