
from pydantic import BaseModel, ConfigDict
from typing import Optional


class NewsCreate(BaseModel):
    title: str
    description: str
    category: str
    location: Optional[str] = None
    is_breaking: bool = False


class NewsUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    location: Optional[str] = None
    is_breaking: Optional[bool] = None


class NewsResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    location: Optional[str]
    status: str
    is_breaking: bool

    model_config = ConfigDict(from_attributes=True)
