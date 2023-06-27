import prompt
import random
from brain_games.games import games_logic as gl


def calc():
    gl.welcome()
    print('What is the result of the expression?')
    while gl.points < 3:
        number1 = random.randint(1, 30)
        number2 = random.randint(1, 10)
        operations = ['+', '-', '*']
        operator = random.choice(operations)
        print(f'Question: {number1} {operator} {number2}')
        answer = prompt.string("Your answer: ")
        if operator == '+':
            correct_answer = number1 + number2
        elif operator == '-':
            correct_answer = number1 - number2
        else:
            correct_answer = number1 * number2
        gl.play_game(answer, str(correct_answer))
