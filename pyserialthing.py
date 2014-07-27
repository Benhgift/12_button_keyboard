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
                'qw':'a', 'we':'i', 'er':'o',
                'qe':'e', 'qr':'h', 'wr':'t',
                'ui':'s', 'io':'n', 'op':'b',
                'uo':'c', 'up':'d', 'ip':'f',
                'qu':'g', 'qi':'j', 'qo':'k',
                'qp':'l', 'wu':'m', 'wi':'p',
                'wo':'q', 'wp':'r',
                'eu':'u', 'ei':'v', 'eo':'w',
                'ep':'x', 'ru':'y', 'ri':'z',
                'ro':'.', 'rp':'<-',
                'n':' ', 'm':'-crtl-',
                'c':'-mod', 'v':'-shift-'
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

