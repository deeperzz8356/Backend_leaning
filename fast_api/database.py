from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRESQL_USER="postgres"
POSTGRESQL_PASSWORD="Deep"
POSTGRESQL_HOST="localhost"
POSTGRESQL_PORT="5432"
POSTGRESQL_DBNAME="postgres"

DATABASE_URL = f"postgresql+psycopg2://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DBNAME}"

#connection
engine=create_engine(DATABASE_URL)

#session
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
Base=declarative_base()