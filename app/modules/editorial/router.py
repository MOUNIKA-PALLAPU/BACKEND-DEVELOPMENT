
from fastapi import APIRouter, HTTPException

from app.modules.editorial import service
from app.modules.editorial.schemas import (
    EditorialCreate,
    EditorialUpdate,
    EditorialResponse
)

router = APIRouter(
    prefix="/editorial",
    tags=["Editorial"]
)


# Assign submission to an editor
@router.post("/assign", response_model=EditorialResponse)
def assign_submission(data: EditorialCreate):
    editorial = service.assign_submission(data.model_dump())

    if editorial is None:
        raise HTTPException(
            status_code=404,
            detail="Submission not found"
        )

    return editorial


# Get all editorial records
@router.get("/", response_model=list[EditorialResponse])
def get_all_editorial():
    return service.get_all_editorial()


# Get editorial record by ID
@router.get("/{editorial_id}", response_model=EditorialResponse)
def get_editorial(editorial_id: int):
    editorial = service.get_editorial_by_id(editorial_id)

    if editorial is None:
        raise HTTPException(
            status_code=404,
            detail="Editorial record not found"
        )

    return editorial


# Update editorial record
@router.put("/{editorial_id}", response_model=EditorialResponse)
def update_editorial(
    editorial_id: int,
    data: EditorialUpdate
):
    editorial = service.update_editorial(
        editorial_id,
        data.model_dump(exclude_unset=True)
    )

    if editorial is None:
        raise HTTPException(
            status_code=404,
            detail="Editorial record not found"
        )

    return editorial


# Approve submission
@router.put("/{editorial_id}/approve", response_model=EditorialResponse)
def approve_submission(editorial_id: int):
    editorial = service.approve_submission(editorial_id)

    if editorial is None:
        raise HTTPException(
            status_code=404,
            detail="Editorial record not found"
        )

    return editorial


# Reject submission
@router.put("/{editorial_id}/reject", response_model=EditorialResponse)
def reject_submission(editorial_id: int):
    editorial = service.reject_submission(editorial_id)

    if editorial is None:
        raise HTTPException(
            status_code=404,
            detail="Editorial record not found"
        )

    return editorial


# Request corrections
@router.put("/{editorial_id}/correction")
def request_correction(editorial_id: int, comments: str):
    editorial = service.request_correction(
        editorial_id,
        comments
    )

    if editorial is None:
        raise HTTPException(
            status_code=404,
            detail="Editorial record not found"
        )

    return editorial
