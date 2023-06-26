#!/usr/bin/env python3
import prompt
import random


def is_even():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    points = 0
    while points < 3:
        number = random.randint(1, 100)
        correct = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer == correct:
            points += 1
            print('Correct!')
        else:
            print(
                f'"{answer}" is wrong answer ;( Correct answer was "{correct}".'
                )
            print(f'Let`s try again, {name}!')
            points = 4
    if points == 3:
        print(f'Congratulations, {name}!')


def main():
    is_even()


if __name__ == '__main__':
    main()
