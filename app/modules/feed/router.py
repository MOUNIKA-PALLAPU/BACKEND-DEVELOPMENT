
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.async_session import get_db
from app.modules.feed import service
from app.modules.news.schemas import NewsResponse

router = APIRouter(prefix="/feed", tags=["Feed"])


@router.get("/home", response_model=list[NewsResponse])
async def home_feed(db: AsyncSession = Depends(get_db)):
    return await service.get_home_feed(db)


@router.get("/local", response_model=list[NewsResponse])
async def local_feed(
    location: str,
    db: AsyncSession = Depends(get_db)
):
    return await service.get_local_feed(db, location)


@router.get("/breaking", response_model=list[NewsResponse])
async def breaking_feed(db: AsyncSession = Depends(get_db)):
    return await service.get_breaking_feed(db)
