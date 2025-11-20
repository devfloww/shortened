from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from datetime import datetime, timezone

from app.db.database import Base

class Link(Base):
    __tablename__ = "links"
    
    slug = Column(String(7), primary_key=True, unique=True, nullable=False, index=True)
    originalLink = Column(String, nullable=False)
    createdAt = Column(DateTime(timezone=True), default=datetime.now(tz=timezone.utc), server_default=func.now())
    visitedCount = Column(Integer, default=0)
