
from pydantic import BaseModel
from typing import Optional


# Schema for assigning a submission to an editor
class EditorialCreate(BaseModel):
    submission_id: int
    editor_name: str


# Schema for updating editorial review
class EditorialUpdate(BaseModel):
    editor_name: Optional[str] = None
    comments: Optional[str] = None


# Schema for editorial response
class EditorialResponse(BaseModel):
    id: int
    submission_id: int
    editor_name: str
    comments: Optional[str] = None
    status: str
