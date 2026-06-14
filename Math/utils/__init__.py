def automationBiasFunction(integrity: bool, rating: int, confidence: float) -> float:
    """
    Berechnet einen normalisierten Automation-Bias-Score.

    Die Funktion skaliert einen Likert-Rating-Wert (1–5) und die Confidence (0–100)
    auf einen Wert zwischen 0 und 1 und kombiniert diese linear.

    Wenn integrity True ist, wird 0 zurückgegeben (keine Verzerrung).

    Parameters:
    ----------
    integrity : bool
        Wenn True, wird angenommen, dass keine Verzerrung vorliegt → Ergebnis = 0.
    rating : int
        Likert-Skala von 1 bis 5 (inklusive).
    confidence : float
        Konfidenzwert im Bereich 0 bis 100.

    Returns:
    -------
    float
        Normalisierter Automation-Bias-Score zwischen 0 und 1.

    Raises:
    ------
    ValueError
        Wenn rating nicht im Bereich 1–5 liegt oder confidence nicht in 0–100 ist.
    """

    if integrity:
        return 0.0

    if rating < 1 or rating > 5:
        raise ValueError(f"rating must be in range 1–5, got {rating}")

    if confidence < 0 or confidence > 100:
        raise ValueError(f"confidence must be in range 0–100, got {confidence}")

    return ((rating - 1) / 4) * (confidence / 100)


def parse_bool(val) -> bool:
    if val is None:
        return False

    v = str(val).strip().lower()

    if v in ("true", "1", "yes", "ja", "wahr"):
        return True
    elif v in ("false", "0", "no", "nein", "falsch"):
        return False

    raise ValueError(f"Cannot parse boolean: {val}")


ROUNDING = 4
