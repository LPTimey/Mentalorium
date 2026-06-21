import pandas as pd
from dataclasses import dataclass
from typing import List
from utils.likert import Likert5, Likert7
from utils import parse_bool, ROUNDING


@dataclass
class UEQScale:
    item_1: Likert7
    item_2: Likert7
    item_3: Likert7
    item_4: Likert7
    importance: Likert7

    @property
    def mean_score(self) -> float:
        return (
            int(self.item_1) + int(self.item_2) + int(self.item_3) + int(self.item_4)
        ) / 4


@dataclass
class UEQIntuitiveUse:
    difficult_easy: Likert7
    illogical_logical: Likert7
    not_plausible_plausible: Likert7
    inconclusive_conclusive: Likert7
    importance: Likert7

    @property
    def mean_score(self) -> float:
        return (
            int(self.difficult_easy)
            + int(self.illogical_logical)
            + int(self.not_plausible_plausible)
            + int(self.inconclusive_conclusive)
        ) / 4

    @classmethod
    def from_df_row(cls, row: pd.Series, round_idx: int) -> "UEQIntuitiveUse":
        return cls(
            difficult_easy=Likert7(
                int(row[f"intuitive use - difficult <> easy (round {round_idx})"])
            ),
            illogical_logical=Likert7(
                int(row[f"intuitive use - illogical <> logical (round {round_idx})"])
            ),
            not_plausible_plausible=Likert7(
                int(
                    row[
                        f"intuitive use - not plausible <> plausible (round {round_idx})"
                    ]
                )
            ),
            inconclusive_conclusive=Likert7(
                int(
                    row[
                        f"intuitive use - inconclusive <> conclusive (round {round_idx})"
                    ]
                )
            ),
            importance=Likert7(
                int(row[f"intuitive use - importance (round {round_idx})"])
            ),
        )

    def to_dict(self, round_idx: int) -> dict:
        return {
            f"intuitive use - difficult <> easy (round {round_idx})": int(
                self.difficult_easy
            ),
            f"intuitive use - illogical <> logical (round {round_idx})": int(
                self.illogical_logical
            ),
            f"intuitive use - not plausible <> plausible (round {round_idx})": int(
                self.not_plausible_plausible
            ),
            f"intuitive use - inconclusive <> conclusive (round {round_idx})": int(
                self.inconclusive_conclusive
            ),
            f"intuitive use - importance (round {round_idx})": int(self.importance),
            f"intuitive use mean (round {round_idx})": round(self.mean_score, ROUNDING),
        }


@dataclass
class UEQTrustworthiness:
    useless_useful: Likert7
    implausible_plausible: Likert7
    untrustworthy_trustworthy: Likert7
    inaccurate_accurate: Likert7
    importance: Likert7

    @property
    def mean_score(self) -> float:
        return (
            int(self.useless_useful)
            + int(self.implausible_plausible)
            + int(self.untrustworthy_trustworthy)
            + int(self.inaccurate_accurate)
        ) / 4

    @classmethod
    def from_df_row(cls, row: pd.Series, round_idx: int) -> "UEQTrustworthiness":
        return cls(
            useless_useful=Likert7(
                int(
                    row[
                        f"trustworthiness of content - useless <> useful (round {round_idx})"
                    ]
                )
            ),
            implausible_plausible=Likert7(
                int(
                    row[
                        f"trustworthiness of content - implausible <> plausible (round {round_idx})"
                    ]
                )
            ),
            untrustworthy_trustworthy=Likert7(
                int(
                    row[
                        f"trustworthiness of content - untrustworthy <> trustworthy (round {round_idx})"
                    ]
                )
            ),
            inaccurate_accurate=Likert7(
                int(
                    row[
                        f"trustworthiness of content - inaccurate <> accurate (round {round_idx})"
                    ]
                )
            ),
            importance=Likert7(
                int(row[f"trustworthiness of content - importance (round {round_idx})"])
            ),
        )

    def to_dict(self, round_idx: int) -> dict:
        return {
            f"trustworthiness of content - useless <> useful (round {round_idx})": int(
                self.useless_useful
            ),
            f"trustworthiness of content - implausible <> plausible (round {round_idx})": int(
                self.implausible_plausible
            ),
            f"trustworthiness of content - untrustworthy <> trustworthy (round {round_idx})": int(
                self.untrustworthy_trustworthy
            ),
            f"trustworthiness of content - inaccurate <> accurate (round {round_idx})": int(
                self.inaccurate_accurate
            ),
            f"trustworthiness of content - importance (round {round_idx})": int(
                self.importance
            ),
            f"trustworthiness mean (round {round_idx})": round(
                self.mean_score, ROUNDING
            ),
        }


@dataclass
class UEQResponseBehavior:
    artificial_natural: Likert7
    unpleasant_pleasant: Likert7
    unlikeable_likeable: Likert7
    boring_entertaining: Likert7
    importance: Likert7

    @property
    def mean_score(self) -> float:
        return (
            int(self.artificial_natural)
            + int(self.unpleasant_pleasant)
            + int(self.unlikeable_likeable)
            + int(self.boring_entertaining)
        ) / 4

    @classmethod
    def from_df_row(cls, row: pd.Series, round_idx: int) -> "UEQResponseBehavior":
        return cls(
            artificial_natural=Likert7(
                int(
                    row[
                        f"response behavior - artificial <> natural (round {round_idx})"
                    ]
                )
            ),
            unpleasant_pleasant=Likert7(
                int(
                    row[
                        f"response behavior - unpleasant <> pleasant (round {round_idx})"
                    ]
                )
            ),
            unlikeable_likeable=Likert7(
                int(
                    row[
                        f"response behavior - unlikeable <> likeable (round {round_idx})"
                    ]
                )
            ),
            boring_entertaining=Likert7(
                int(
                    row[
                        f"response behavior - boring <> entertaining (round {round_idx})"
                    ]
                )
            ),
            importance=Likert7(
                int(row[f"response behavior - importance (round {round_idx})"])
            ),
        )

    def to_dict(self, round_idx: int) -> dict:
        return {
            f"response behavior - artificial <> natural (round {round_idx})": int(
                self.artificial_natural
            ),
            f"response behavior - unpleasant <> pleasant (round {round_idx})": int(
                self.unpleasant_pleasant
            ),
            f"response behavior - unlikeable <> likeable (round {round_idx})": int(
                self.unlikeable_likeable
            ),
            f"response behavior - boring <> entertaining (round {round_idx})": int(
                self.boring_entertaining
            ),
            f"response behavior - importance (round {round_idx})": int(self.importance),
            f"response behavior mean (round {round_idx})": round(
                self.mean_score, ROUNDING
            ),
        }


@dataclass
class UEQResponseQuality:
    inappropriate_appropriate: Likert7
    useless_useful: Likert7
    not_helpful_helpful: Likert7
    unintelligent_intelligent: Likert7
    importance: Likert7

    @property
    def mean_score(self) -> float:
        return (
            int(self.inappropriate_appropriate)
            + int(self.useless_useful)
            + int(self.not_helpful_helpful)
            + int(self.unintelligent_intelligent)
        ) / 4

    @classmethod
    def from_df_row(cls, row: pd.Series, round_idx: int) -> "UEQResponseQuality":
        return cls(
            inappropriate_appropriate=Likert7(
                int(
                    row[
                        f"response quality - inappropriate <> appropriate (round {round_idx})"
                    ]
                )
            ),
            useless_useful=Likert7(
                int(row[f"response quality - useless <> useful (round {round_idx})"])
            ),
            not_helpful_helpful=Likert7(
                int(
                    row[
                        f"response quality - not helpful <> helpful (round {round_idx})"
                    ]
                )
            ),
            unintelligent_intelligent=Likert7(
                int(
                    row[
                        f"response quality - unintelligent <> intelligent (round {round_idx})"
                    ]
                )
            ),
            importance=Likert7(
                int(row[f"response quality - importance (round {round_idx})"])
            ),
        )

    def to_dict(self, round_idx: int) -> dict:
        return {
            f"response quality - inappropriate <> appropriate (round {round_idx})": int(
                self.inappropriate_appropriate
            ),
            f"response quality - useless <> useful (round {round_idx})": int(
                self.useless_useful
            ),
            f"response quality - not helpful <> helpful (round {round_idx})": int(
                self.not_helpful_helpful
            ),
            f"response quality - unintelligent <> intelligent (round {round_idx})": int(
                self.unintelligent_intelligent
            ),
            f"response quality - importance (round {round_idx})": int(self.importance),
            f"response quality mean (round {round_idx})": round(
                self.mean_score, ROUNDING
            ),
        }


@dataclass
class UEQClarity:
    poorly_grouped_well_grouped: Likert7
    unstructured_structured: Likert7
    disordered_ordered: Likert7
    disorganized_organized: Likert7
    importance: Likert7

    @property
    def mean_score(self) -> float:
        return (
            int(self.poorly_grouped_well_grouped)
            + int(self.unstructured_structured)
            + int(self.disordered_ordered)
            + int(self.disorganized_organized)
        ) / 4

    @classmethod
    def from_df_row(cls, row: pd.Series, round_idx: int) -> "UEQClarity":
        return cls(
            poorly_grouped_well_grouped=Likert7(
                int(
                    row[f"clarity - poorly grouped <> well grouped (round {round_idx})"]
                )
            ),
            unstructured_structured=Likert7(
                int(row[f"clarity - unstructured <> structured (round {round_idx})"])
            ),
            disordered_ordered=Likert7(
                int(row[f"clarity - disordered <> ordered (round {round_idx})"])
            ),
            disorganized_organized=Likert7(
                int(row[f"clarity - disorganized <> organized (round {round_idx})"])
            ),
            importance=Likert7(int(row[f"clarity - importance (round {round_idx})"])),
        )

    def to_dict(self, round_idx: int) -> dict:
        return {
            f"clarity - poorly grouped <> well grouped (round {round_idx})": int(
                self.poorly_grouped_well_grouped
            ),
            f"clarity - unstructured <> structured (round {round_idx})": int(
                self.unstructured_structured
            ),
            f"clarity - disordered <> ordered (round {round_idx})": int(
                self.disordered_ordered
            ),
            f"clarity - disorganized <> organized (round {round_idx})": int(
                self.disorganized_organized
            ),
            f"clarity - importance (round {round_idx})": int(self.importance),
            f"clarity mean (round {round_idx})": round(self.mean_score, ROUNDING),
        }


@dataclass
class UEQRiskHandling:
    hardly_apparent_easily_apparent: Likert7
    not_fed_back_timely_fed_back_timely: Likert7
    difficult_to_understand_easy_to_understand: Likert7
    unstoppable_stoppable: Likert7
    importance: Likert7

    @property
    def mean_score(self) -> float:
        return (
            int(self.hardly_apparent_easily_apparent)
            + int(self.not_fed_back_timely_fed_back_timely)
            + int(self.difficult_to_understand_easy_to_understand)
            + int(self.unstoppable_stoppable)
        ) / 4

    @classmethod
    def from_df_row(cls, row: pd.Series, round_idx: int) -> "UEQRiskHandling":
        return cls(
            hardly_apparent_easily_apparent=Likert7(
                int(
                    row[
                        f"risk handling - hardly apparent <> easily apparent (round {round_idx})"
                    ]
                )
            ),
            not_fed_back_timely_fed_back_timely=Likert7(
                int(
                    row[
                        f"risk handling - not fed back in a timely manner <> fed back in a timely manner (round {round_idx})"
                    ]
                )
            ),
            difficult_to_understand_easy_to_understand=Likert7(
                int(
                    row[
                        f"risk handling - indicated in a manner which is difficult to understand <> indicated in a manner which is easy to understand (round {round_idx})"
                    ]
                )
            ),
            unstoppable_stoppable=Likert7(
                int(
                    row[f"risk handling - unstoppable <> stoppable (round {round_idx})"]
                )
            ),
            importance=Likert7(
                int(row[f"risk handling - importance (round {round_idx})"])
            ),
        )

    def to_dict(self, round_idx: int) -> dict:
        return {
            f"risk handling - hardly apparent <> easily apparent (round {round_idx})": int(
                self.hardly_apparent_easily_apparent
            ),
            f"risk handling - not fed back in a timely manner <> fed back in a timely manner (round {round_idx})": int(
                self.not_fed_back_timely_fed_back_timely
            ),
            f"risk handling - indicated in a manner which is difficult to understand <> indicated in a manner which is easy to understand (round {round_idx})": int(
                self.difficult_to_understand_easy_to_understand
            ),
            f"risk handling - unstoppable <> stoppable (round {round_idx})": int(
                self.unstoppable_stoppable
            ),
            f"risk handling - importance (round {round_idx})": int(self.importance),
            f"risk handling mean (round {round_idx})": round(self.mean_score, ROUNDING),
        }


@dataclass
class UEQRound:
    intuitive_use: UEQIntuitiveUse
    trustworthiness: UEQTrustworthiness
    response_behavior: UEQResponseBehavior
    response_quality: UEQResponseQuality
    clarity: UEQClarity
    risk_handling: UEQRiskHandling

    @classmethod
    def from_df_row(cls, row: pd.Series, round_idx: int) -> "UEQRound":
        return cls(
            intuitive_use=UEQIntuitiveUse.from_df_row(row, round_idx),
            trustworthiness=UEQTrustworthiness.from_df_row(row, round_idx),
            response_behavior=UEQResponseBehavior.from_df_row(row, round_idx),
            response_quality=UEQResponseQuality.from_df_row(row, round_idx),
            clarity=UEQClarity.from_df_row(row, round_idx),
            risk_handling=UEQRiskHandling.from_df_row(row, round_idx),
        )

    def to_dict(self, round_idx: int) -> dict:
        row = {}

        row.update(self.intuitive_use.to_dict(round_idx))
        row.update(self.trustworthiness.to_dict(round_idx))
        row.update(self.response_behavior.to_dict(round_idx))
        row.update(self.response_quality.to_dict(round_idx))
        row.update(self.clarity.to_dict(round_idx))
        row.update(self.risk_handling.to_dict(round_idx))

        return row
