"""In-class exercise on functions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i = 0
    
    while i < n - 1:
        love_note += love(to) + "\n"
        i += 1
    
    love_note += love(to)
    
    return love_note