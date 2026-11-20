
from app.modules.news import mock_store
from app.modules.news.schemas import NewsCreate, NewsUpdate


# Create a new news article
def create_news(data: NewsCreate):
    global_next_id = mock_store.next_news_id

    news = {
        "id": global_next_id,
        "title": data.title,
        "description": data.description,
        "category": data.category,
        "location": data.location,
        "status": "draft",
        "is_breaking": data.is_breaking
    }

    mock_store.news_data.append(news)
    mock_store.next_news_id += 1

    return news


# Get all news articles
def get_all_news():
    return mock_store.news_data


# Get news by ID
def get_news_by_id(news_id: int):
    for news in mock_store.news_data:
        if news["id"] == news_id:
            return news

    return None



# Update existing news
def update_news(news_id: int, data: NewsUpdate):
    news = get_news_by_id(news_id)

    if news is None:
        return None

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        news[key] = value

    return news

# Delete news by ID
def delete_news(news_id: int):
    news = get_news_by_id(news_id)

    if news is None:
        return False

    mock_store.news_data.remove(news)

    return True
