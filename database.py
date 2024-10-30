from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import Settings
engine = create_engine(
    Settings.database_url,
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
    
)