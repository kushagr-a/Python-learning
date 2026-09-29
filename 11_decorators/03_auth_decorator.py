from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user="admin", *args, **kwargs):
        if user == "admin":
            return func(*args, **kwargs)
        else:
            return "Access denied"
    return wrapper

@require_admin
def delete_user(username, user="admin"):
    print(f"Deleting {username}")
    return f"{username} deleted"

print(delete_user("user1"))
print(delete_user("user2", user="admin"))
print(delete_user.__name__)