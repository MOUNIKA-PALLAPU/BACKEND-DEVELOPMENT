
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.news.models import News
from app.modules.news.schemas import NewsCreate, NewsUpdate


async def create_news(db: AsyncSession, data: NewsCreate):
    news = News(**data.model_dump())

    db.add(news)
    await db.commit()
    await db.refresh(news)

    return news


async def get_all_news(db: AsyncSession):
    result = await db.execute(
        select(News).order_by(News.id.desc())
    )
    return result.scalars().all()


async def get_news_by_id(db: AsyncSession, news_id: int):
    result = await db.execute(
        select(News).where(News.id == news_id)
    )
    return result.scalar_one_or_none()


async def update_news(
    db: AsyncSession,
    news_id: int,
    data: NewsUpdate
):
    news = await get_news_by_id(db, news_id)

    if news is None:
        return None

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(news, key, value)

    await db.commit()
    await db.refresh(news)

    return news


async def delete_news(db: AsyncSession, news_id: int):
    news = await get_news_by_id(db, news_id)

    if news is None:
        return False

    await db.delete(news)
    await db.commit()

    return True
