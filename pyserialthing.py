import serial
import msvcrt
from itertools import permutations

class Keypress():
	def __init__(self):
		self.keymap = {
				'qwe':'a', 'wer':'i', 'qer':'o',
				'qwr':'e', 'uio':'s', 'iop':'t',
				'uop':'h', 'uip':'n', 'qwu':'b',
				'qwi':'c', 'qwo':'d', 'qwp':'f',
				'weu':'g', 'wei':'j', 'weo':'k',
				'wep':'l', 'qeu':'m', 'qei':'p',
				'qeo':'q', 'qep':'r',
				'qri':'u', 'qro':'v', 'qrp':'w',
				'qru':'x', 'qri':'y', 'qro':'z',
				}
		self.current_keys = []

	def get_press(self):
		if len(self.current_keys) >= 3:
			keys = permutations(self.current_keys)
			for key in keys:
				try:
					print self.keymap[''.join(key)],
				except:
					pass
			print '---'
			self.current_keys = []
		else:
			self.current_keys.append(msvcrt.getch())
			if 1 in self.current_keys:
				sys.exit()

k = Keypress()
while True:
	k.get_press()

#ser = serial.Serial("COM3", 9600)

#for x in range(10):
#	x = ser.read()
#	print x

