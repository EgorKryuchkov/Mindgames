import prompt


points = 0
name = ''


def welcome():
    global name
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def play_game(answer, correct_answer):
    global name
    global points
    if answer == correct_answer:
        print('Correct!')
        points += 1
    else:
        print(
            f'"{answer}" is wrong answer ;( Correct answer was "{correct_answer}".'
            )
        print(f'Let`s try again, {name}!')
        points = 4
    if points == 3:
        print(f'Congratulations, {name}!')

