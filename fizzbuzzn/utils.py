def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
