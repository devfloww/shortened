from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db import models
from app.utils import link_to_slug

async def create_link(db: AsyncSession, original_link: str) -> models.Link:
    """Create a shortened link or return existing one if same URL already exists."""
    slug = link_to_slug(original_link)

    # existing = db.query(models.Link).filter_by(slug=slug).first()
    result = await db.execute(select(models.Link).where(models.Link.slug==slug))
    existing = result.scalar_one_or_none()
    if existing:
        return existing  # return model instance

    new_link = models.Link(slug=slug, originalLink=original_link)
    db.add(new_link)
    await db.commit()
    await db.refresh(new_link)

    return new_link


async def get_link_by_slug(db: AsyncSession, slug: str) -> models.Link | None:
    result = await db.execute(select(models.Link).where(models.Link.slug==slug))
    return result.scalar_one_or_none()

async def increment_visited_count(db: AsyncSession, link: models.Link):
    link.visitedCount += 1
    await db.commit()
    await db.refresh(link)
