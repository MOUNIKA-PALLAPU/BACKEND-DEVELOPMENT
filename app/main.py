from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine

from app.modules.users import models

from app.modules.auth.routes import router as auth_router
from app.modules.users.router import router as users_router
from app.modules.mock.routes import router as mock_router
from app.modules.news.router import router as news_router
from app.modules.feed.router import router as feed_router
from app.modules.submissions.router import router as submissions_router
from app.modules.editorial.router import router as editorial_router


app = FastAPI(
    title="MSR News Backend",
    description="MSR News Channel Management System APIs",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Register Authentication routes
app.include_router(auth_router)

# Register Users routes
app.include_router(users_router)

# Register Mock routes
app.include_router(mock_router)

# Register News routes
app.include_router(news_router)

# Register Feed routes
app.include_router(feed_router, prefix="/api/v1")

# Register Submissions routes
app.include_router(submissions_router, prefix="/api/v1")

# Register Editorial routes
app.include_router(editorial_router, prefix="/api/v1")


@app.get("/")
def home():
    return {
        "message": "MSR News Backend API is running successfully"
    }
