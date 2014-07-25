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

# alg:
# make a 2d DP table. 
# x axis = all combinations of n-mers from the chord set, (1), (2), (2,4,5) etc
#   this represents usable combos, start at smallest
# y axis = all combinations of n-mers from the alphabet
#   this represents usable letters, start at smallest
# fill in table, for example for a (2,4,5) and (s,t,e), it would look at the 
#   the best 2mer combinations that used (2,4), (4,5) and (2,5) for each 2mer of (s,t,e)
#   and attach to the best one after computing how much better the score is after adding 
#   the third letter (s,t or e). A total or n*n comparisons

def _find_the_next_combo(data): 
    # try each of the combinations, pick the one that combines for the biggest gains
        # find next letter for each combo
    chosen_combo = None
    for combo in data.combinations:
        # to find the value for this combo we need to compare all the reprocussions of this
        break
    return data

def _find_the_next_letter(data): 
    # for each letter find the best one to use for thise combo
    return data

def find_best_buttons(buttons, aphabet):
    empty_data = RunningData([], aphabet[:], buttons[:])
    initialized_data = _init_buttons(empty_data)
    finished_data = _find_the_next_combo(initialized_data)
    return finished_data

print find_best_buttons(buttons, alphabet)
