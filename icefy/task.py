from dataclasses import dataclass


@dataclass
class Task:
    text: str
    impact: float
    confidence: float
    ease: float