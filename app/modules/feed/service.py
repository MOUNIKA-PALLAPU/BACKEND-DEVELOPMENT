
from app.modules.news import mock_store


# Get published news only
def get_published_news():
    return [
        news for news in mock_store.news_data
        if news["status"] == "published"
    ]


# Home Feed
def get_home_feed():
    return get_published_news()


# Local Feed
def get_local_feed(location: str):
    return [
        news for news in get_published_news()
        if news["location"]
        and news["location"].lower() == location.lower()
    ]


# Breaking News Feed
def get_breaking_feed():
    return [
        news for news in get_published_news()
        if news["is_breaking"] is True
    ]


# Trending News Feed
def get_trending_feed():
    return get_published_news()
