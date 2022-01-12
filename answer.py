from dataclasses import dataclass

from question import Question


@dataclass
class Answer:
    question: Question
    answer: int

    @property
    def correct(self) -> bool:
        return self.question.correct_option == self.answer
