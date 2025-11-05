from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

# Globals and configs
DATABASE_URL = str(os.getenv("DATABASE_URL"))
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False}, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

async def get_db():
    with SessionLocal() as conn:
        yield conn

    # db = SessionLocal()
    # try:
    #     yield db
    # except Exception:
    #     raise HTTPException(500, "Internal Server Error")
    # finally:
    #     db.close()