from sqlmodel import SQLModel, create_engine, Session
from backend.models import *  # Import your SQLModel models

# Database connection URL
# DATABASE_URL = "postgresql://username:password@localhost/dbname" # template
DATABASE_URL = "postgresql://api:letMein123!@localhost/tmi-db" ### SECURITY ISSUE, fix this


# Create the SQLModel engine
engine = create_engine(DATABASE_URL)

def create_database():
    """
    Create tables in the PostgreSQL database based on the SQLModel definitions.
    """
    SQLModel.metadata.create_all(engine)

def get_session(): # why is this function here?
    """
    Get a session for the database.
    """
    with Session(engine) as session:
        yield session

if __name__ == "__main__":
    create_database()
    print("Database and tables are set up.")
