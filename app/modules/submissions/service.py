
from app.modules.submissions import mock_store


# Create a new news submission
def create_submission(data: dict):
    global next_submission_id

    submission = {
        "id": mock_store.next_submission_id,
        "title": data["title"],
        "description": data["description"],
        "category": data["category"],
        "location": data.get("location"),
        "reporter_name": data["reporter_name"],
        "status": "submitted"
    }

    mock_store.submissions_data.append(submission)
    mock_store.next_submission_id += 1

    return submission


# Get all submissions
def get_all_submissions():
    return mock_store.submissions_data


# Get submission by ID
def get_submission_by_id(submission_id: int):
    for submission in mock_store.submissions_data:
        if submission["id"] == submission_id:
            return submission

    return None


# Update submission
def update_submission(submission_id: int, data: dict):
    submission = get_submission_by_id(submission_id)

    if submission is None:
        return None

    for key, value in data.items():
        if value is not None:
            submission[key] = value

    return submission


# Delete submission
def delete_submission(submission_id: int):
    submission = get_submission_by_id(submission_id)

    if submission is None:
        return False

    mock_store.submissions_data.remove(submission)

    return True
