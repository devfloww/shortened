from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

from app.db.database import Base

class Link(Base):
    __tablename__ = "links"

    slug = Column(String(7), primary_key=True, unique=True, nullable=False, index=True)
    originalLink = Column(String, nullable=False)
    createdAt = Column(DateTime, default=datetime.now(tz=timezone.utc))
    visitedCount = Column(Integer, default=0)
