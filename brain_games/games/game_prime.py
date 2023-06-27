import prompt
import random
from brain_games.games import games_logic as gl


def is_prime():
    gl.welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while gl.points < 3:
        number = random.randint(2, 100)
        for i in range(2, 11):
            if i == number:
                correct_answer = 'yes'
                break
            if number % i == 0:
                correct_answer = 'no'
                break
            if i == 10:
                correct_answer = 'yes'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        gl.play_game(answer, correct_answer)
