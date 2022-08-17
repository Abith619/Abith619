import werkzeug


class DatabaseNotExists(werkzeug.exceptions.HTTPException):
    code = 440
    description = (
        "Database not found"
    )
