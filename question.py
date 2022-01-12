from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    question_text: str
    options: List[str]
    correct_option: int

