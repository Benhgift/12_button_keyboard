from itertools import combinations
from string import ascii_lowercase
from collections import namedtuple as nt
import copy

buttons = list(combinations(range(8), 2))
reserved = [(0,7), (3,4)] # backspace, space
alphabet = list(ascii_lowercase)
alphabet_2mers = combinations(alphabet, 2)
letter_combination_frequency_data = dict([[y,x] for x,y in enumerate(alphabet_2mers)])

Button = nt('button', 'combo letter')
RunningData = nt('data', 'buttons letters combinations')

def _init_buttons(data):
    data = copy.deepcopy(data)
    if not data.buttons:
        button1 = Button((0, 1), 's')
        data.buttons.append(button1)
        data.letters.remove(button1.letter)
        data.combinations.remove(button1.combo)
    return data

def _find_the_next_piece(data): 
    # try each of the combinations, pick the one that combines for the biggest gains
    return data

def find_best_buttons(buttons, aphabet):
    empty_data = RunningData([], aphabet[:], buttons[:])
    initialized_data = _init_buttons(empty_data)
    finished_data = _find_the_next_piece(initialized_data)
    return finished_data

print find_best_buttons(buttons, alphabet)
