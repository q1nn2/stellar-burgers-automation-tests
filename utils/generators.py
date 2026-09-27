from uuid import uuid4


def generate_user_data():
    suffix = uuid4().hex

    return {
        "email": f"autotest_{suffix}@example.com",
        "password": f"Password_{suffix[:12]}",
        "name": f"User_{suffix[:8]}",
    }
