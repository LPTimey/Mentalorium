from __future__ import annotations
from utils import automationBiasFunction, ROUNDING
from utils.likert import Likert5
from utils.parsers import parse_bool
from dataclasses import dataclass
from enum import StrEnum
import pandas as pd
import statistics
from typing import List

# Eventuell pydantic statt dataclass aber unsure


class Persona(StrEnum):
    Amina = "Amina"
    Aylin = "Aylin"
    Lena = "Lena"
    Martina = "Martina"
    Mathias = "Mathias"


@dataclass
class Vignette:
    persona: Persona
    integrity: bool
    rating: Likert5
    confidence: float

    @property
    def bias_score(self) -> float:
        return automationBiasFunction(self.integrity, self.rating, self.confidence)

    @classmethod
    def from_df_row(cls, row: pd.Series, round_idx: int) -> "Vignette":
        return cls(
            persona=Persona(row[f"case (round {round_idx})"].strip()),
            integrity=parse_bool(row[f"correctness (round {round_idx})"]),
            rating=Likert5(int(row[f"rating (round {round_idx})"])),
            confidence=float(row[f"confidence (round {round_idx})"]),
        )

    def to_dict(self, round_idx: int) -> dict:
        return {
            f"persona (round {round_idx})": str(self.persona),
            f"integrity (round {round_idx})": str(self.integrity).lower(),
            f"rating (round {round_idx})": int(self.rating),
            f"confidence (round {round_idx})": float(self.confidence),
            f"bias_score (round {round_idx})": round(self.bias_score, ROUNDING),
        }


@dataclass
class Session:
    usefulness_gen: Likert5
    usefulness_men: Likert5
    acceptability_gen: Likert5
    acceptability_men: Likert5
    vignette1: Vignette
    vignette2: Vignette
    vignette3: Vignette

    @property
    def mean_bias_score(self) -> float:
        values = [
            self.vignette1.bias_score,
            self.vignette2.bias_score,
            self.vignette3.bias_score,
        ]

        filtered = [x for x in values if x != 0]

        return statistics.mean(filtered) if filtered else 0.0

    @classmethod
    def from_df_row(cls, row: pd.Series) -> "Session":
        return cls(
            usefulness_gen=Likert5(int(row["usefulness"])),
            usefulness_men=Likert5(int(row["usefulness (mental health)"])),
            acceptability_gen=Likert5(int(row["acceptability"])),
            acceptability_men=Likert5(int(row["acceptability (mental health)"])),
            vignette1=Vignette.from_df_row(row, 1),
            vignette2=Vignette.from_df_row(row, 2),
            vignette3=Vignette.from_df_row(row, 3),
        )

    def to_dict(self) -> dict:
        row = {
            "usefulness": int(self.usefulness_gen),
            "acceptability": int(self.acceptability_gen),
            "usefulness (mental health)": int(self.usefulness_men),
            "acceptability (mental health)": int(self.acceptability_men),
            "mean_bias_score": round(self.mean_bias_score, ROUNDING),
        }
        row.update(self.vignette1.to_dict(1))
        row.update(self.vignette2.to_dict(2))
        row.update(self.vignette3.to_dict(3))
        return row


@dataclass
class Participant:
    nickname: str
    age: int
    gender: str
    is_active: bool
    session1: Session
    session2: Session

    @property
    def mean_bias_score(self) -> float:
        return statistics.mean(
            [
                self.session1.mean_bias_score,
                self.session2.mean_bias_score,
            ]
        )

    @classmethod
    def parse_many_from_csvs(
        cls, session1_df: pd.DataFrame, session2_df: pd.DataFrame
    ) -> List["Participant"]:
        participants = []

        for (_, row1), (_, row2) in zip(session1_df.iterrows(), session2_df.iterrows()):
            participants.append(cls.from_df_rows(row1, row2))

        return participants

    @classmethod
    def from_df_rows(
        cls, session1_row: pd.Series, session2_row: pd.Series
    ) -> "Participant":
        return cls(
            nickname=session1_row["nickname"],
            age=int(session1_row["age"]),
            gender=session1_row["gender"],
            is_active=parse_bool(session1_row["disclaimer (round 1)"]),
            session1=Session.from_df_row(session1_row),
            session2=Session.from_df_row(session2_row),
        )

    def to_dict(self) -> dict:
        row = {
            "nickname": self.nickname,
            "age": self.age,
            "gender": self.gender,
            "is_active_group": str(self.is_active).lower(),
            "mean_bias_score": round(self.mean_bias_score, ROUNDING),
        }

        postfix = " (session 1)"
        row.update({(k + postfix): v for k, v in self.session1.to_dict().items()})
        postfix = " (session 2)"
        row.update({(k + postfix): v for k, v in self.session2.to_dict().items()})

        return row

    @staticmethod
    def participants_to_df(participants: List[Participant]) -> pd.DataFrame:
        return pd.DataFrame([p.to_dict() for p in participants])
