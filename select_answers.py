from typing import List, Dict

from PyInquirer import prompt

from answer import Answer
from question import Question


def select_answers(questions: List[Question]) -> str:
    answers = get_user_input(questions)
    summary = evaluate_questionaire(answers)
    return summary


def get_user_input(questions: List[Question]) -> List[Answer]:
    question_list = _format_questions(questions)
    raw_answers = prompt(question_list)
    answers = []
    for question, answer_key in zip(questions, raw_answers):
        answer_string = raw_answers[answer_key]
        answer_index = question.options.index(answer_string)
        answers.append(Answer(question, answer_index))
    return answers


def _format_questions(questions: List[Question]) -> List[Dict]:
    return [
        {
            "type": "rawlist",
            "name": index,
            "message": f"{question.question_text}?",
            "choices": question.options,
        }
        for index, question in enumerate(questions)
    ]


def evaluate_questionaire(answers: List[Answer]) -> str:
    num_correct = _count_correct_answers(answers)
    summary = f"\n\n\n{num_correct} von {len(answers)} wurden richtig beantworted ({num_correct/len(answers)*100}%)\n\n"
    for answer in answers:
        summary += f"{answer.question.question_text}?\n"
        if answer.correct:
            summary += f"\tDeine Antwort {answer.question.options[answer.answer]} war richtig.\n"
        else:
            summary += f"\t Deine Antwort {answer.question.options[answer.answer]} war falsch.\n"
            summary += f"\t Richtige Antwort: {answer.question.options[answer.question.correct_option]}\n"
    return summary

def _count_correct_answers(answers):
    count = 0
    for answer in answers:
        if answer.correct:
            count += 1
    return count
