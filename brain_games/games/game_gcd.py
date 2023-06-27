import prompt
import random
from brain_games.games import games_logic as gl


def find_gcd():
    gl.welcome()
    print('Find the greatest common divisor of given numbers.')
    while gl.points < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)

        def euclid(n1, n2):
            big_numb = n1 if n1 > n2 else n2
            small_numb = n2 if n2 < n1 else n1
            remainder = big_numb % small_numb
            if remainder == 0:
                return small_numb
            return euclid(small_numb, remainder)
        correct_answer = euclid(number1, number2)
        print(f'Question: {number1} {number2}')
        answer = prompt.string('Your answer: ')
        gl.play_game(answer, str(correct_answer))
