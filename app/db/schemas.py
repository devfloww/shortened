from pydantic import BaseModel, HttpUrl
from datetime import datetime

class LinkCreate(BaseModel):
    url: HttpUrl

class LinkResponse(BaseModel):
    id: int
    original_link: str
    slug: str
    createAt: datetime
    visitedCount: int

    class Config:
        from_attributes = True
