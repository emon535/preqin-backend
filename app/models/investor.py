from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db.database import Base
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Investor(Base):
    __tablename__ = 'investors'

    id = Column(Integer, primary_key=True)
    investor_name = Column(String, unique=True, nullable=False)
    investor_type = Column(String)
    investor_country = Column(String)
    investor_date_added = Column(Date)
    investor_last_updated = Column(Date)

    # Define the relationship with Commitment
    commitments = relationship('Commitment', back_populates='investor')

