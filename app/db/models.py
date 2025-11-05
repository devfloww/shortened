from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

from app.db.database import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    originan_link = Column(String, nullable=False)
    slug = Column(String(7), unique=True, nullable=False, index=True)
    createdAt = Column(DateTime, default=datetime.now(tz=timezone.utc))
    visitedCount = Column(Integer, default=0)
