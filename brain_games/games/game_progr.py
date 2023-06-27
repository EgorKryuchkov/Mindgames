import prompt
import random
from brain_games.games import games_logic as gl


def find_numb():
    gl.welcome()
    print('What number is missing in the progression?')
    while gl.points < 3:
        first = random.randint(1, 50)
        diff = random.randint(1, 20)
        length = random.randint(5, 10)
        progression = [first]
        i = 0
        while i < length:
            first += diff
            progression.append(first)
            i += 1
        correct_answer = random.choice(progression)
        progression = ['...' if x == correct_answer else x for x in progression]
        print(f'Question: {progression}')
        answer = prompt.string('Your answer: ')
        gl.play_game(answer, str(correct_answer))
