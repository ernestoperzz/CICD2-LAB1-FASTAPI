import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = os.getenv(
"DATABASE_URL",
"sqlite:///./app.db",
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()