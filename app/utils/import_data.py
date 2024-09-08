import pandas as pd
from sqlalchemy.orm import Session
from db.database import engine, SessionLocal
import models
from sqlalchemy.exc import SQLAlchemyError

def import_data_from_csv(file_path: str):
    models.Base.metadata.create_all(bind=engine)
    df = pd.read_csv(file_path)
    db = SessionLocal()

    try:
        investor_dict = {}
        for _, row in df.iterrows():
            investor_name = row['Investor Name']
            investor_type = row['Investory Type']
            investor_country = row['Investor Country']
            investor_date_added = pd.to_datetime(row['Investor Date Added']).date()
            investor_last_updated = pd.to_datetime(row['Investor Last Updated']).date()

            if investor_name not in investor_dict:
                investor = models.Investor(
                    investor_name=investor_name,
                    investor_type=investor_type,
                    investor_country=investor_country,
                    investor_date_added=investor_date_added,
                    investor_last_updated=investor_last_updated
                )
                db.add(investor)
                db.commit()
                db.refresh(investor)
                investor_dict[investor_name] = investor.id
            else:
                investor_id = investor_dict[investor_name]

            commitment = models.Commitment(
                investor_id=investor_dict[investor_name],
                asset_class=row['Commitment Asset Class'],
                amount=row['Commitment Amount'],
                currency=row['Commitment Currency']
            )
            db.add(commitment)

        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    import_data_from_csv('./../../data/data.csv')  # Provide the path to your CSV file
