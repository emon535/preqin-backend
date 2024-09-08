from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Commitment(Base):
    __tablename__ = "commitments"

    id = Column(Integer, primary_key=True, index=True)
    investor_id = Column(Integer, ForeignKey("investors.id"), nullable=False)
    asset_class = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)

    # Relationships
    investor = relationship("Investor", back_populates="commitments")
