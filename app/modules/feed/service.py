
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.news.models import News


async def get_home_feed(db: AsyncSession):
    result = await db.execute(
        select(News)
        .where(News.status == "published")
        .order_by(News.created_at.desc())
        .limit(20)
    )
    return result.scalars().all()


async def get_local_feed(db: AsyncSession, location: str):
    result = await db.execute(
        select(News)
        .where(
            News.status == "published",
            News.location == location
        )
        .order_by(News.created_at.desc())
    )
    return result.scalars().all()


async def get_breaking_feed(db: AsyncSession):
    result = await db.execute(
        select(News)
        .where(
            News.status == "published",
            News.is_breaking == True
        )
        .order_by(News.created_at.desc())
    )
    return result.scalars().all()
