from click import command, option, Path

from parse_file import parse_file
from select_answers import select_answers



@command()
@option("--question_filename", type=Path(dir_okay=False, exists=True), default='questions.txt')
def main(question_filename):
    questions = parse_file(question_filename)
    summary = select_answers(questions)
    print(summary)


if __name__ == "__main__":
    main()