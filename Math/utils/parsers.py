def parse_bool(val) -> bool:
    if val is None:
        return False

    v = str(val).strip().lower()

    if v in ("true", "1", "yes", "ja", "wahr"):
        return True
    elif v in ("false", "0", "no", "nein", "falsch"):
        return False

    raise ValueError(f"Cannot parse boolean: {val}")
