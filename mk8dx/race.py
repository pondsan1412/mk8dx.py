from __future__ import annotations

from typing import Optional
from mk8dx.data import Track
from rank import Rank


class Race:

    __slots__ = (
        '__format',
        '__ranks',
        'track'
    )

    def __init__(self, format: int, track: Optional[Track] = None) -> None:
        self.__format = format
        self.__ranks: list[Rank] = []
        self.track: Optional[Track] = track

    @property
    def ranks(self) -> list[Rank]:
        return self.__ranks

    @property
    def format(self) -> int:
        return self.__format

    @property
    def scores(self) -> list[int]:
        return list(map(lambda r: r.score, self.ranks))

    def is_valid(self) -> bool:
        return len(self.ranks) == 12 // len(self.format)

    def add_ranks_from_text(self, text: str) -> None:
        ranks = Rank.get_ranks_from_text(text=text, format=self.format, ranks=self.ranks)
        self.__ranks.extend(ranks)