#import serial
#import msvcrt
import sys
from itertools import permutations
import tty
from datetime import datetime
from datetime import timedelta

tty.setcbreak(sys.stdin)

class Keypress():
    def __init__(self):
        self.keymap = {
            'io':'a', 'ui':'b', 'qp':'c',
            'we':'d', 'ro':'e', 'qr':'f',
            'wo':'g', 'eu':'h', 'ri':'i',
            'er':'j', 'wi':'k', 'wu':'l',
            'wp':'m', 'qu':'n', 'eo':'o',
            'qi':'p', 'qo':'q', 'up':'r',
            'ep':'s', 'qw':'t', 'wr':'u',
            'qe':'v', 'ip':'w', 'uo':'x',
            'rp':'y', 'ru':'z',
            'ei':'.', 'op':'<-',
            'n':' ', 'm':'-crtl-',
            'c':'-mod-', 'v':'-shift-'
            }
        self.current_keys = []
        self.last_time = datetime.now()
        self.this_time = datetime.now()
        self.max_time = timedelta(milliseconds=200)

    def _clear_if_took_too_long(self):
        self.this_time = datetime.now()
        if self.this_time - self.last_time > self.max_time:
            self.last_time = datetime.now()
            self.current_keys = [self.current_keys[-1]]

    def _try_to_print_a_key(self):
        keys = permutations(self.current_keys)
        for key in keys:
            try:
                x = self.keymap[''.join(key)]
                sys.stdout.write(x)
                self.current_keys = []
            except:
                pass
        if len(self.current_keys) > 2:
            self.current_keys = []

    def get_press(self):
        self.current_keys.append(sys.stdin.read(1))
        self._clear_if_took_too_long()
        self._try_to_print_a_key()


k = Keypress()
while True:
    k.get_press()

#ser = serial.Serial("COM3", 9600)

#for x in range(10):
#    x = ser.read()
#    print x

