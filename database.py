from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config

DB_URL=f"mysql+pymysql://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

engine = create_engine(DB_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)