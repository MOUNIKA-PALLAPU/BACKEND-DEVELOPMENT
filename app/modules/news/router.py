from fastapi import APIRouter, HTTPException

from app.modules.news import mock_service as service
from app.modules.news.schemas import (
    NewsCreate,
    NewsUpdate,
    NewsResponse
)

router = APIRouter(
    prefix="/news",
    tags=["News"]
)


@router.post("/", response_model=NewsResponse)
def create_news(data: NewsCreate):
    return service.create_news(data)


@router.get("/", response_model=list[NewsResponse])
def get_all_news():
    return service.get_all_news()

@router.get("/{news_id}", response_model=NewsResponse)
def get_news(news_id: int):
    news = service.get_news_by_id(news_id)

    if news is None:
        raise HTTPException(
            status_code=404,
            detail="News not found"
        )

    return news


@router.put("/{news_id}", response_model=NewsResponse)
def update_news(news_id: int, data: NewsUpdate):
    news = service.update_news(news_id, data)

    if news is None:
        raise HTTPException(
            status_code=404,
            detail="News not found"
        )

    return news

@router.delete("/{news_id}")
def delete_news(news_id: int):
    deleted = service.delete_news(news_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="News not found"
        )

    return {
        "message": "News deleted successfully"
    }