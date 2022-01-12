from typing import List

from question import Question

def parse_file(filename:str)->List[Question]:
    with open(filename, "r") as question_file:
        raw_string = '\n'.join(question_file.readlines())
    questions_strings = split_questions(raw_string)
    questions = []
    for question_string in questions_strings:
        questions.append(build_question(question_string))
    return questions

def split_questions(input_string:str)->List[str]:
    questions = input_string.split('?')
    return [question.strip() for question in questions if question.strip() != '']

def build_question(question_string:str)->Question:
    lines = question_string.splitlines()
    lines = [line.strip() for line in lines if line.strip() != ""]
    correct_index = 0
    for index, line in enumerate(lines[1:]):
        if line.startswith('*'):
            correct_index = index
            lines[index+1] = line.replace("*", "")
    lines.append("Ich weiß es nicht")
    return Question(lines[0], lines[1:], correct_index)