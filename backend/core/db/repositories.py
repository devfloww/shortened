from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from core.db.models import User, Link
from core.db.schemas import *

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: UserCreate):
        pass

    async get_user(self, id: UUID):
        pass