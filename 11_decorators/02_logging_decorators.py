from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_activity
def order_chai(name):
    print(f"ordering {name}")
    return f"{name} is ready"

print(order_chai("Ginger chai"))
print(order_chai.__name__)