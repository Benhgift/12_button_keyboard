# I'm trying to find the optimal button->letter map for the keyboard.
# These are the facts:
#     The keyboard uses 8 buttons for letters, 2-mer combination map 1:1 to letters
#         ex: button 0 and button 1 at the same time map to 's'
#     Buttons that are often pressed in succession shouldn't have their combination overlap
#         ex: 's' mapped to (0,1) shouldn't then have 't' mapped to (0,2)
#     Succession buttons like that that are very common should occur on different hands
#         ex: 's' mapped to (0,1) (left hand) would then benefit from 't' being on (5,6) (right hand)

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
