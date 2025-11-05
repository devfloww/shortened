from pydantic import BaseModel
from datetime import datetime

class LinkCreate(BaseModel):
    url: str

class LinkResponse(BaseModel):
    slug: str
    original_link: str
    shortened_link: str
    createAt: datetime
    visitedCount: int

    class Config:
        from_attributes = True
