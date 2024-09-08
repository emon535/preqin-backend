
# app/models/commitment.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Commitment(Base):
    __tablename__ = 'commitments'
    
    id = Column(Integer, primary_key=True, index=True)
    investor_id = Column(Integer, ForeignKey('investors.id'))
    asset_class = Column(String)
    amount = Column(Float)
    currency = Column(String)
    
    investor = relationship("Investor", back_populates="commitments")