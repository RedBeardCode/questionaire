import pytest

from parse_file import build_question, split_questions
from question import Question


@pytest.mark.parametrize(
    ["input_string", "expected_strings"],
    [
        pytest.param(
            "?a\nb\nc\n*d\n?e\nf\ng\n*h", ["a\nb\nc\n*d", "e\nf\ng\n*h"], id="valid"
        ),
        pytest.param(
            "?a\nb\n\nc\n*d\n?e\nf\ng\n*h",
            ["a\nb\n\nc\n*d", "e\nf\ng\n*h"],
            id="additional newline in answers",
        ),
        pytest.param(
            "?a\nb\nc\n*d\n\n\n?e\nf\ng\n*h",
            ["a\nb\nc\n*d", "e\nf\ng\n*h"],
            id="additional newline between questions",
        ),
        pytest.param(
            "\n?a\nb\nc\n*d\n?e\nf\ng\n*h\n",
            ["a\nb\nc\n*d", "e\nf\ng\n*h"],
            id="newlines in start and end",
        ),
    ],
)
def test_split_questions(input_string, expected_strings):
    output_strings = split_questions(input_string.strip())
    assert output_strings == expected_strings


@pytest.mark.parametrize(["question_string", "expected_questions"], [
    pytest.param(
        """
        Einfache Frage
        Falsche Antwort
        *Richtige Antwort
        """,
        Question("Einfache Frage", ["Falsche Antwort", "Richtige Antwort", "Ich weiß es nicht"], 1),
        id="Valid single questions"
    ),
    pytest.param(
        """

        Einfache Frage
        Falsche Antwort
        *Richtige Antwort

        """,
        Question("Einfache Frage", ["Falsche Antwort", "Richtige Antwort", "Ich weiß es nicht"], 1),
        id="Newline in start and end"
    ),
    pytest.param(
        """
        Einfache Frage
        
        Falsche Antwort
        
        *Richtige Antwort
        """,
        Question("Einfache Frage", ["Falsche Antwort", "Richtige Antwort", "Ich weiß es nicht"], 1),
        id="Newline between answers"
    )
])
def test_build_questions(question_string, expected_questions):
    questions = build_question(question_string)
    assert questions == expected_questions