from datetime import datetime, timezone
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID as _UUID

from core.db.database import Base
from uuid import uuid4

user_generated_links = Table(
    "user_generated_links",
    Base.metadata,
    Column("user_id", _UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
    Column("link_id", _UUID(as_uuid=True), ForeignKey("links.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"
    
    id = Column(_UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    generated_links = relationship(
        "Link",
        secondary=user_generated_links,
        back_populates="owner"
    )

class Link(Base):
    __tablename__ = "links"

    id = Column(_UUID(as_uuid=True), primary_key=True, default=uuid4)
    original_link = Column(String, nullable=False)
    shortened_link = Column(String, unique=True, nullable=False)
    createdAt = Column(DateTime, default=datetime.now(timezone.utc))
    expiresAt = Column(DateTime, nullable=True)
    visitCount = Column(Integer, default=0)
    privacy = Column(String, default="public")

    owner = relationship(
        "User",
        secondary=user_generated_links,
        back_populates="generated_links"
    )    
