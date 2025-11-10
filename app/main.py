from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db import models, schemas, database
from app import crud

# Globals and Configs
models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

@app.post("/shorten")
async def create_short_link(
    link: schemas.LinkCreate,
    request: Request,
    db_session: Session = Depends(database.get_db)
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

