import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.investor import Investor
from app.models.commitment import Commitment
from app.db.database import Base
from datetime import datetime

# Database URL (example: SQLite)
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return None

def import_csv_to_db(file_path: str):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        investor_map = {}  # To map investor names to their database records

        for row in reader:
            investor_name = row['Investor Name']
            if investor_name not in investor_map:
                investor = Investor(
                    investor_name=investor_name,
                    investor_type=row['Investory Type'],
                    investor_country=row['Investor Country'],
                    investor_date_added=parse_date(row['Investor Date Added']),
                    investor_last_updated=parse_date(row['Investor Last Updated'])
                )
                session.add(investor)
                session.commit()
                investor_map[investor_name] = investor  # Map investor name to investor object

            # Create and add commitment record
            commitment = Commitment(
                investor_id=investor_map[investor_name].id,
                asset_class=row['Commitment Asset Class'],
                amount=float(row['Commitment Amount']),
                currency=row['Commitment Currency']
            )
            session.add(commitment)

        session.commit()

if __name__ == "__main__":
    import_csv_to_db('./data.csv')
