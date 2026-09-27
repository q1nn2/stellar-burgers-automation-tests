REQUEST_TIMEOUT = 15
INVALID_INGREDIENT_HASH = "00000000000000000000000"

REQUIRED_USER_FIELDS = (
    "email",
    "password",
    "name",
)

INVALID_LOGIN_CASES = (
    ("email", "unknown_user@example.com"),
    ("password", "wrong_password"),
)

INVALID_LOGIN_CASE_IDS = (
    "invalid_email",
    "invalid_password",
)
