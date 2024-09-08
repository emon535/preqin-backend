from fastapi import APIRouter

from . import commitments 
from . import investors  

api_router = APIRouter()

api_router.include_router(investors.router, prefix="/investors", tags=["investors"])
api_router.include_router(commitments.router, prefix="/commitments", tags=["commitments"])
