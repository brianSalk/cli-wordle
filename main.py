from sys import stderr, exit
import random
import os
from collections import Counter
from copy import copy
from termcolor import colored
from time import sleep
def read_word():
    word_added = True
    while True:
        display_board(guesses, word_added)
        word = input()
        word = word.upper().strip()
        if len(word) != 5:
            print(colored(f'not a five letter word', 'red'))
            sleep(1.5)
        elif word + '\n' not in words:
            print(colored(f'not a valid word', 'red'))
            sleep(1.5)
        else:
            return word
        word_added = False

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
    return colored_guess

def display_board(board, word_added):
    os.system('clear')
    if word_added:
        for each in guesses[:-1]:
            print("".join(each))
        if len(guesses) > 0: 
            for letter in guesses[-1]:
                sleep(.4)
                print(letter,end="",flush=True)
            print()
    else:
        for each in guesses:
            print("".join(each))


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
        current_guess = read_word()
        colored_guess = color_guess(current_guess, answer_count)
        guesses.append(colored_guess)
        if (current_guess == answer or guess_count == GUESS_LIMIT):
            display_board(guesses, True)
            if current_guess == answer:
                print(f'CONGRATES!, you guessed correctly in {guess_count} tries')
            else:
                print(f'the correct word was {answer}')
            y_n = input('play again? (y/N)')
            if y_n.strip().upper() == 'Y':
                guess_count = 0
                r = random.randint(0,len(words))
                answer = words[r][:-1]
                answer_count = Counter(answer)
                guesses = []
            else:
                print('goodby!')
                exit()
        guess_count+=1
    
    
      

	
