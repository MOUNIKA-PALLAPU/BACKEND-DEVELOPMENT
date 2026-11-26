
from pydantic import BaseModel
from typing import Optional


# Schema for creating a submission
class SubmissionCreate(BaseModel):
    title: str
    description: str
    category: str
    location: Optional[str] = None
    reporter_name: str


# Schema for updating a submission
class SubmissionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    location: Optional[str] = None


# Schema for submission response
class SubmissionResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    location: Optional[str]
    reporter_name: str
    status: str
