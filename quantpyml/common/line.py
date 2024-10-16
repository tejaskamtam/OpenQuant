from dataclasses import dataclass

@dataclass
class Line:
    period: int | None = None
    values: list[float]
