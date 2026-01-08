from sqlalchemy import Column, Integer, String
from app.database import Base

class Repo(Base):
    __tablename__ = "repo"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String, index=True)
    name = Column(String, index=True)
    stars = Column(Integer, default=0)
    url = Column(String)