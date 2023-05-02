from sys import stderr, exit, argv
import random
import os
from collections import Counter
from copy import copy
from termcolor import colored
from time import sleep
import argparse
def set_english():
    WELCOME = 'Welcome to command-line wordle'
    PRESS_ANY_KEY='press any key to continue'
    NOT_FIVE='not a five letter word'
    NOT_IN_MY_DICT='not a valid word'
    CORRECT='CONGRATES!, you guessed correctly in {guess_count} tries'
    INCORRECT='the correct word was {answer}'
    PLAY_AGAIN=f'play again?'
    GOODBY='goodby'
    return WELCOME,PRESS_ANY_KEY,NOT_FIVE, NOT_IN_MY_DICT, CORRECT, INCORRECT, PLAY_AGAIN, GOODBY, 'english'
def set_german():
    WELCOME = 'Willkommen zu command-line Wordle'
    PRESS_ANY_KEY='Drücken Sie eine beliebige Taste, um fortzufahren'
    NOT_FIVE='nich ein fünf buchstäbiges Wort'
    NOT_IN_MY_DICT='Das Wort kenne ich nicht'
    CORRECT='Richtig!  Das hat Ihnen {guess_count} Versuche gekostet.'
    INCORRECT='Die rightige Antwort war {answer}'
    PLAY_AGAIN=f'Wieder spielen? (j/N)'
    GOODBY='Tschuß!'
    return WELCOME,PRESS_ANY_KEY,NOT_FIVE, NOT_IN_MY_DICT, CORRECT, INCORRECT, PLAY_AGAIN, GOODBY, 'german'
def read_word():
    word_added = True
    while True:
        display_board(guesses, word_added)
        word = input()
        word = word.upper().strip()
        if len(word) != 5:
            print(colored(NOT_FIVE, 'red'))
            sleep(1.5)
        elif word + '\n' not in words:
            print(colored(NOT_IN_MY_DICT, 'red'))
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
                print(letter, end="",flush=True)
            print()
    else:
        for each in guesses:
            print("".join(each))

def play_again(y_n):
    if LANG == 'english' and y_n.strip().upper() == 'Y':
        return True
    elif LANG == 'german' and y_n.strip().upper() == 'J':
        return True

parser = argparse.ArgumentParser()
parser.add_argument('user_language')

args = parser.parse_args()
if __name__ == '__main__':
    
    if args.user_language.endswith('english'):
        WELCOME,PRESS_ANY_KEY,NOT_FIVE, NOT_IN_MY_DICT, CORRECT, INCORRECT, PLAY_AGAIN, GOODBY, LANG = set_english()
    elif args.user_language.endswith('german'):
        WELCOME,PRESS_ANY_KEY,NOT_FIVE, NOT_IN_MY_DICT, CORRECT, INCORRECT, PLAY_AGAIN, GOODBY, LANG = set_german()
    with open(LANG) as f:
        words = f.readlines()
        r = random.randint(0,len(words)-1)
        answer = words[r][:-1]
    GUESS_LIMIT = 6
    answer_count = Counter(answer)
    guesses = []
    guess_count = 1
    os.system('clear')
    # print welcome message
    print(colored(WELCOME,'blue').center(90))
    print(colored(PRESS_ANY_KEY.upper(),'magenta').center(90))
    input()
    os.system('clear')
    while True:
        # del_Me
        current_guess = read_word()
        colored_guess = color_guess(current_guess, answer_count)
        guesses.append(colored_guess)
        if (current_guess == answer or guess_count == GUESS_LIMIT):
            display_board(guesses, True)
            if current_guess == answer:
                print(colored(CORRECT.format(guess_count=guess_count), 'green'))
            else:
                print(colored(INCORRECT.format(answer=answer), 'red'))
            y_n = input(PLAY_AGAIN)
            if play_again(y_n):
                guess_count = 0
                r = random.randint(0,len(words))
                answer = words[r][:-1]
                answer_count = Counter(answer)
                guesses = []
            else:
                print(GOODBY)
                exit()
        guess_count+=1
    
    
      

	
