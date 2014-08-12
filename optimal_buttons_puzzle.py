# I'm trying to find the optimal button->letter map for the keyboard.
# first get the number of occurences of each 2mer in a text
# make a genetic algorithm that optimizes based on that

from itertools import combinations
from functools import partial
from itertools import repeat
from multiprocessing import Pool
from string import ascii_lowercase
from collections import defaultdict as ddict
from collections import namedtuple as nt
from random import shuffle
from random import random
from copy import deepcopy as dcopy

buttons = list(combinations(range(8), 2))
reserved = (6,7) #backspace
buttons.remove(reserved)

alphabet = list(ascii_lowercase) + ['.']
alphabet_2mers = combinations(alphabet, 2)

with open('training_text.txt', 'r') as f:
    text = f.read()

#Button = nt('button', 'combo letter')
#Creature = nt('creat', 'buttons score')
class Button(object):
    def __init__(self, combo, letter):
        self.__dict__.update(locals())
    def __repr__(self):
        return "Button %s %s" % (str(self.combo), str(self.letter))
    def __str__(self):
        return "Button %s %s" % (str(self.combo), str(self.letter))
class Creature(object):
    def __init__(self, buttons, score):
        self.__dict__.update(locals())

def get_2mer_freq_data(text):
    def _get_freq_data(text, mer):
        mer_dict = ddict(int)
        for x in range(len(text)-mer+1):
            text_segment = text[x:x+mer]
            mer_dict[text_segment] += 1
        return mer_dict
    return _get_freq_data(text, 2)
def _make_rand_creature(alphabet, blank_buttons):
    _alpha = dcopy(alphabet)
    blank_buttons = dcopy(blank_buttons)
    shuffle(_alpha)
    buttons = []
    for x,y in zip(blank_buttons, _alpha):
        buttons.append(Button(x, y))
    return Creature(buttons, 0)
def _make_starting_creatures(num_to_make, alphabet, blank_buttons):
    creatures = []
    for x in range(num_to_make):
        creatures.append(_make_rand_creature(alphabet, blank_buttons))
    return creatures
def _compute_button_score(button, creature, freq_data):
    score = 0
    x = set(button.combo)
    for other_button in creature.buttons:
        y = set(other_button.combo)
        if not x.intersection(y):
            score += freq_data[button.letter + other_button.letter]
            score += freq_data[other_button.letter + button.letter]
    return score
def _compute_score(creature, freq_data):
    score = 0
    for button in creature.buttons:
        score += _compute_button_score(button, creature, freq_data)
    return Creature(creature.buttons, score)
def _compute_data_for_all(creatures, freq_data):
    new_creatures = []
    for creature in creatures:
        new_creatures.append(_compute_score(creature, freq_data))
    return new_creatures
def _make_mutant(creature, mutations):
    new_creature = dcopy(creature)
    for x in range(mutations):
        but_len = len(new_creature.buttons)
        button1 = new_creature.buttons[int(random()*but_len)]
        button2 = new_creature.buttons[int(random()*but_len)]
        new_creature.buttons.remove(button1)
        new_creature.buttons.append(Button(button1.combo, button2.letter))
        if button1 != button2:
            new_creature.buttons.remove(button2)
            new_creature.buttons.append(Button(button2.combo, button1.letter))
    return new_creature
def _breed_new_creatures(creatures, best_creature, top_perc=3, mutations=4):
    ordered_creatures = sorted(creatures, key=lambda x: x.score, reverse=True)
    count = len(ordered_creatures)
    our_count = int(count*(.01*top_perc))
    best_creatures = ordered_creatures[0:our_count]
    new_creatures = []
    for x in creatures:
        _creat = best_creatures[int(random()*our_count)]
        newc = _make_mutant(_creat, mutations)
        new_creatures.append(newc)
    return new_creatures
def _get_best(creatures, best_creature):
    ordered_creatures = sorted(creatures, key=lambda x: x.score, reverse=True)
    print 'max min of generation ' + str(ordered_creatures[0].score) + ' ' + str(ordered_creatures[-1].score)
    if not best_creature:
        return ordered_creatures[0]
    if ordered_creatures[0].score > best_creature.score:
        return ordered_creatures[0]
    else:
        return best_creature
def get_good_combination(freq_data, generations, alphabet, buttons):
    creatures = _make_starting_creatures(2000, alphabet, buttons)
    creatures = _compute_data_for_all(creatures, freq_data)
    best_creature = _get_best(creatures, None)
    for x in range(generations):
        print 'working on generation ' + str(x)
        print 'best ' + str(best_creature.score)
        creatures = _breed_new_creatures(creatures, best_creature, top_perc=5, mutations=1)
        creatures = _compute_data_for_all(creatures, freq_data)
        best_creature = _get_best(creatures, best_creature)
    return best_creature

freq_data = get_2mer_freq_data(text)
pool = Pool(processes=4)
get_good_combos = partial(get_good_combination, freq_data, 50, alphabet)

best_creatures = pool.map_async(get_good_combos, repeat(buttons, 4)).get(99999)
for best in best_creatures:
    with open('best_combo', 'a') as f:
        best_buts = sorted([x for x in best.buttons], key=lambda x: x.letter)
        f.writelines([str(x)+'\n' for x in best_buts])
        f.writelines(str(best.score)+'\n')
