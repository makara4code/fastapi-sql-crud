from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    "sqlite:///./my-db.db", connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# DRY: Don't repeat yourself
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
