from sqlalchemy.orm import Session

from app.db import models
from app.utils import link_to_slug

def create_link(db: Session, original_link: str) -> models.Link:
    slug = link_to_slug(original_link)
    # existing_link = db.query(models.Link).filter_by(slug=slug).first()
    # if existing_link:
    #     return existing_link
    
    new_link = models.Link(slug=slug, originalLink=original_link)
    db.add(new_link)
    db.commit()
    db.refresh(new_link)

    return new_link

def get_link_by_slug(db: Session, slug: str) -> models.Link:
    return db.query(models.Link).filter(models.Link.slug == slug).first()

def increment_visited_count(db: Session, link: models.Link):
    link.visitedCount += 1
    db.commit()
    db.refresh(link)
