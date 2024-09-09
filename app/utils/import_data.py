import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.investor import Investor
from app.models.commitment import Commitment
from app.db.database import Base
from datetime import datetime

from app.core.config import Settings


engine = create_engine(Settings().DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
Base.metadata.create_all(bind=engine)



def parse_date(date_str):
    
    try:
        return datetime.strptime(date_str, '%Y-%m-%d') if date_str else None
    except ValueError:
        return None

def get_or_create_investor(investor_name, investor_type, investor_country, date_added, date_updated):
   
    investor = session.query(Investor).filter(Investor.investor_name == investor_name).first()
    
    if not investor:
        investor = Investor(
            investor_name=investor_name,
            investor_type=investor_type,
            investor_country=investor_country,
            investor_date_added=date_added,
            investor_last_updated=date_updated
        )
        session.add(investor)
        session.flush() 
    
    return investor

def import_csv_to_db(file_path: str):

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Create or get investor
            investor = get_or_create_investor(
                investor_name=row['Investor Name'],
                investor_type=row['Investory Type'],
                investor_country=row['Investor Country'],
                date_added=parse_date(row['Investor Date Added']),
                date_updated=parse_date(row['Investor Last Updated'])
            )

            # Create and add commitment record
            commitment = Commitment(
                investor_id=investor.id,
                asset_class=row['Commitment Asset Class'],
                amount=float(row['Commitment Amount']),
                currency=row['Commitment Currency']
            )
            session.add(commitment)

        # Commit session at the end of the process for better performance
        session.commit()

if __name__ == "__main__":
    import_csv_to_db('./data.csv')
