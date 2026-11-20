
from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine

from app.modules.users import models

from app.modules.auth.routes import router as auth_router
from app.modules.users.router import router as users_router
from app.modules.mock.routes import router as mock_router
from app.modules.news.router import router as news_router


app = FastAPI(
    title="MSR News Backend",
    description="MSR News Channel Management System APIs",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Register authentication routes
app.include_router(auth_router)

# Register users routes
app.include_router(users_router)

# Register mock routes
app.include_router(mock_router)

# Register news routes
app.include_router(news_router)


@app.get("/")
def home():
    return {
        "message": "MSR News Backend API is running successfully"
    }
