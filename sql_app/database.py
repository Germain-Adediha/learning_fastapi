# DATABASE CONNECTION( POSTGRE )

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_url = "postgresql://germain:17mawuko17@localhost/my_db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit= False, autoflush=False,bind=engine)
Base = declarative_base()
