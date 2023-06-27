import prompt
import random
from brain_games.games import games_logic as gl


def is_even():
    gl.welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while gl.points < 3:
        number = random.randint(1, 100)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        gl.play_game(answer, correct_answer)
