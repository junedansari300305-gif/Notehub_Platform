from sqlalchemy import Column, Integer, String # type: ignore
from db_config import Base

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    subject = Column(String(100), nullable=False)
    semester = Column(String(50), nullable=False)
    course = Column(String(100), nullable=False)
    college = Column(String(100), nullable=False)
    pdf_link = Column(String(255), nullable=False)
    youtube_link = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Note(title='{self.title}', subject='{self.subject}')>"
