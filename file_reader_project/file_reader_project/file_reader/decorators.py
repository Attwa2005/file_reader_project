def deco(color: str):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }

    def wrapper(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{colors.get(color, '')}{result}{colors['reset']}"
        return inner
    return wrapper
