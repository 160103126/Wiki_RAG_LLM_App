from sqlmodel import create_engine, Session
from app.config.settings import settings

engine = create_engine(settings.DB_URL, connect_args={"check_same_thread": False})

def get_db():
    with Session(engine) as session:
        yield session