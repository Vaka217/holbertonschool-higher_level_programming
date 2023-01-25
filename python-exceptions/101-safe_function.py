#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError, ValueError, TypeError) as exc:
        print(f"Exception: {exc}", file=sys.stderr)
        return None
