from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import  Base, engine
from app.api.v1 import api_router as v1_api_router  

Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI(
    title="Investor Commitments API",
    description="An API to manage investors and their commitments",
    version="1.0.1",
    author="Preqin"
)

# Allow CORS for the frontend (adjust the origins as per your setup)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers for the API endpoints
# app.include_router(api_investors.router, prefix="/api/v1")
# app.include_router(api_commitments.router, prefix="/api/v1")
app.include_router(v1_api_router, prefix="/api/v1")

# Root endpoint to verify that the API is running
@app.get("/")
def read_root():
    return {"message": "Investor Commitments API is running"}

