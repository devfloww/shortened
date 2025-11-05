from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Globals and configs
DATABASE_URL = str(os.getenv("DATABASE_URL"))
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False}, autocommit=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        pass
    finally:
        db.close()