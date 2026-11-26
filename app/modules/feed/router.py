
from fastapi import APIRouter

from app.modules.feed import service

router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)


@router.get("/home")
def home_feed():
    return service.get_home_feed()


@router.get("/local")
def local_feed(location: str):
    return service.get_local_feed(location)


@router.get("/breaking")
def breaking_feed():
    return service.get_breaking_feed()


@router.get("/trending")
def trending_feed():
    return service.get_trending_feed()
