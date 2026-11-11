from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base # type: ignore

engine = create_engine('sqlite:///notehub.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models.notes  # Import all models here
    Base.metadata.create_all(bind=engine)
