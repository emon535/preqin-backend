from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class Investor(Base):
    __tablename__ = "investors"

    id = Column(Integer, primary_key=True, index=True)
    investor_name = Column(String, nullable=False)
    investor_type = Column(String, nullable=False)
    investor_country = Column(String, nullable=False)
    investor_date_added = Column(DateTime, default=datetime.utcnow)
    investor_last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    commitments = relationship("Commitment", back_populates="investor")

