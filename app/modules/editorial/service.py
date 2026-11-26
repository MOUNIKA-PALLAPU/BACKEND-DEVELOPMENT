
from app.modules.editorial import mock_store
from app.modules.submissions import mock_store as submission_store


# Assign a submission to an editor
def assign_submission(data):
    # Check whether submission exists
    submission = None

    for item in submission_store.submissions_data:
        if item["id"] == data["submission_id"]:
            submission = item
            break

    if submission is None:
        return None

    # Create editorial assignment
    editorial = {
        "id": mock_store.next_editorial_id,
        "submission_id": data["submission_id"],
        "editor_name": data["editor_name"],
        "comments": None,
        "status": "under_review"
    }

    mock_store.editorial_data.append(editorial)
    mock_store.next_editorial_id += 1

    # Update submission status
    submission["status"] = "under_review"

    return editorial


# Get all editorial records
def get_all_editorial():
    return mock_store.editorial_data


# Get editorial record by ID
def get_editorial_by_id(editorial_id: int):
    for item in mock_store.editorial_data:
        if item["id"] == editorial_id:
            return item

    return None


# Update editor assignment or comments
def update_editorial(editorial_id: int, data: dict):
    editorial = get_editorial_by_id(editorial_id)

    if editorial is None:
        return None

    for key, value in data.items():
        if value is not None:
            editorial[key] = value

    return editorial


# Approve a submission
def approve_submission(editorial_id: int):
    editorial = get_editorial_by_id(editorial_id)

    if editorial is None:
        return None

    editorial["status"] = "approved"

    for submission in submission_store.submissions_data:
        if submission["id"] == editorial["submission_id"]:
            submission["status"] = "approved"
            break

    return editorial


# Reject a submission
def reject_submission(editorial_id: int):
    editorial = get_editorial_by_id(editorial_id)

    if editorial is None:
        return None

    editorial["status"] = "rejected"

    for submission in submission_store.submissions_data:
        if submission["id"] == editorial["submission_id"]:
            submission["status"] = "rejected"
            break

    return editorial


# Request corrections
def request_correction(editorial_id: int, comments: str):
    editorial = get_editorial_by_id(editorial_id)

    if editorial is None:
        return None

    editorial["status"] = "correction_requested"
    editorial["comments"] = comments

    for submission in submission_store.submissions_data:
        if submission["id"] == editorial["submission_id"]:
            submission["status"] = "correction_requested"
            break

    return editorial
