
from fastapi import APIRouter, HTTPException

from app.modules.submissions import service
from app.modules.submissions.schemas import (
    SubmissionCreate,
    SubmissionUpdate,
    SubmissionResponse
)

router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"]
)


# Create a new submission
@router.post("/", response_model=SubmissionResponse)
def create_submission(data: SubmissionCreate):
    return service.create_submission(data.model_dump())


# Get all submissions
@router.get("/", response_model=list[SubmissionResponse])
def get_all_submissions():
    return service.get_all_submissions()


# Get submission by ID
@router.get("/{submission_id}", response_model=SubmissionResponse)
def get_submission(submission_id: int):
    submission = service.get_submission_by_id(submission_id)

    if submission is None:
        raise HTTPException(
            status_code=404,
            detail="Submission not found"
        )

    return submission


# Update submission
@router.put("/{submission_id}", response_model=SubmissionResponse)
def update_submission(
    submission_id: int,
    data: SubmissionUpdate
):
    submission = service.update_submission(
        submission_id,
        data.model_dump(exclude_unset=True)
    )

    if submission is None:
        raise HTTPException(
            status_code=404,
            detail="Submission not found"
        )

    return submission


# Delete submission
@router.delete("/{submission_id}")
def delete_submission(submission_id: int):
    deleted = service.delete_submission(submission_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Submission not found"
        )

    return {
        "message": "Submission deleted successfully"
    }
