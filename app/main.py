from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

from app.db import models, schemas, database
from app import crud

# lifespan function
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
        yield
    await database.engine.dispose()

# Globals and Configs
switchedapp = FastAPI(lifespan=lifespan)

@app.post("/shorten")
async def create_short_link(
    link: schemas.LinkCreate,
    request: Request,
    db_session: AsyncSession = Depends(database.get_db)
):
    new_link = crud.create_link(
        db=db_session,
        original_link=link.url,
    )
    base_url = str(request.base_url).rstrip('/')
    shortened_url = f"{base_url}/{new_link.slug}"

    return schemas.LinkResponse(
        slug=str(new_link.slug),
        original_link=str(new_link.originalLink),
        shortened_link=shortened_url,
        createAt=new_link.createdAt,
        visitedCount=new_link.visitedCount
    )

@app.get("/{slug}")
async def redirect_link(
    slug: str,
    db_session: AsyncSession = Depends(database.get_db)
):
    link = crud.get_link_by_slug(db=db_session, slug=slug)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    await crud.increment_visited_count(db=db_session, link=link)
    return RedirectResponse(url=str(link.originalLink))
