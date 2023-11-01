"""
This is the main entry-point to my word game, WORDIE (think Wordle)
"""

import os
from features.game import game
from features.instructions import instructions
# from words import word_list
# from features.api.words import request_word
from scraper.past_words import get_random_word

os.system('clear')

print('\033[36m\033[45mWelcome to WORDIE.\033[37m\033[40m\n')

instructions_query = input('\nWould you like to hear the \033[34mdirections\033[37m? (y/n) ')

if instructions_query.upper() == 'Y' or instructions_query.upper() == 'YES':
    instructions()

ready = input('\nAre you ready to play Wordie!? (y/n)')

if ready == 'y' or ready.upper() == 'YES' or ready.upper() == 'Y':
    game(get_random_word)