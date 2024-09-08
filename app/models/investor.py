from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

class Investor(Base):
    __tablename__ = 'investors'
    
    id = Column(Integer, primary_key=True, index=True)
    investor_name = Column(String, index=True)
    investor_type = Column(String)
    investor_country = Column(String)
    investor_date_added = Column(DateTime)
    investor_last_updated = Column(DateTime)
    

    commitments = relationship("Commitment", back_populates="investor")

