from fastapi import APIRouter

from . import commitments  # Adjust the import according to your file structure
from . import investors  # Adjust the import according to your file structure

# Create an API router for version 1
api_router = APIRouter()

# Include the routes
api_router.include_router(investors.router, prefix="/investors", tags=["investors"])
api_router.include_router(commitments.router, prefix="/commitments", tags=["commitments"])
