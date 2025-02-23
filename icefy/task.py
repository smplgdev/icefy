from dataclasses import dataclass
from enum import Enum


@dataclass
class Task:
    text: str
    impact: float
    confidence: float
    ease: float


def dicts_to_tasks(data: list[dict]) -> list[Task]:
    return [Task(**task) for task in data]


class TaskEnum(str, Enum):
    text = "text"
    impact = "impact"
    confidence = "confidence"
    ease = "ease"
