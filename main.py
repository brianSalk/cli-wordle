from sys import stderr, exit
import random
from collections import Counter
from copy import copy
from termcolor import colored
def read_word(msg):
    while True:
        for each in guesses:
            print(each)
        word = input(msg)
        word = word.upper().strip()
        if len(word) != 5:
            print(f'{word} is not a five letter word', file=stderr)
        elif word + '\n' not in words:
            print(f'{word} is not a valid word', file=stderr)
        else:
            return word

def color_guess(guess, answer_count):
    colored_guess = list(guess)
    counts = copy(answer_count)
    correct_indexes = []
    for i,letter in enumerate(guess):
        if answer[i] == letter:
            colored_guess[i] = colored(letter,'green')
            counts[letter] -= 1
            correct_indexes.append(i)
    for i,letter in enumerate(guess):
        if i in correct_indexes:
            continue
        if counts[letter] > 0:
            colored_guess[i] = colored(letter,'yellow')
            counts[letter] -= 1
        else:
            colored_guess[i] = colored(letter, 'white')
    return "".join(colored_guess)


if __name__ == '__main__':
    with open('words.txt') as f:
        words = f.readlines()
        r = random.randint(0,len(words)-1)
        answer = words[r][:-1]
    GUESS_LIMIT = 6
    answer_count = Counter(answer)
    guesses = []
    guess_count = 1
    while True:
        # del_Me
        msg = f'guess #{guess_count}: '
        current_guess = read_word(msg)
        colored_guess = color_guess(current_guess, answer_count)
        guesses.append(colored_guess)
        if (current_guess == answer or guess_count == GUESS_LIMIT):
            if current_guess == answer:
                print(color_guess)
                print(f'CONGRATES!, you guessed correctly in {guess_count} tries')
            else:
                print(f'the correct word was {answer}')
            y_n = input('play again? (y/N)')
            if y_n.strip().upper() == 'Y':
                guess_count = 0
                r = random.randint(0,len(words))
                answer = words[r][:-1]
            else:
                print('goodby!')
                exit()
        guess_count+=1
    
    
      

	
