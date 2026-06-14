from utils import likert
from dataclasses import dataclass

@dataclass
class Vignette:
    persona: str
    integrity: bool
    rating: Likert5
    confidence: float


@dataclass
class Session:
    usefulness_gen: Likert5
    usefulness_men: Likert5
    acceptability_gen: Likert5
    acceptability_men: Likert5
    vignette1: Vignette
    vignette2: Vignette
    vignette3: Vignette


@dataclass
class Participant:
    nickname: str
    age: int
    lang: str
    gender: str
    is_active: bool
    session1: Session
    session2: Session
