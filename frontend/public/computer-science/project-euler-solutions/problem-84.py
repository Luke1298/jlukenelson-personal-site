import numpy as np


class monopoly:
	def __init__(self, dice_size=6, current_space=0):
		self.dice_size = dice_size
		self.current_space = current_space
		self.board = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
		self.CC = ['GO', 'JAIL', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
		self.CH = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'NR', 'NR', 'NU', '-3', '', '', '', '', '', '']
		np.random.shuffle(self.CC)
		np.random.shuffle(self.CH)
		pass
	def roll(self):
		return np.random.randint(1, self.dice_size+1, 2)
	def ComunityChest(self):
		event = self.CC[0]
		self.CC = np.roll(self.CC, -1)
		if event in self.board:
			self.current_space = self.board.index(event)
	def Chance(self):
		event = self.CH[0]
		self.CH = np.roll(self.CH, -1)
		if not event:
			pass
		elif event in self.board:
			self.current_space = self.board.index(event)
		elif "N" == event[0]:
			while self.board[self.current_space][0] != event[1]:
				self.move(1)
		elif event == "-3":
			self.move(-3)
	def move(self, num_move):
		self.current_space += num_move
		self.current_space %= 40
		if self.board[self.current_space][:2] == "CH":
			self.Chance()
		elif self.board[self.current_space][:2] == "CC":
			self.ComunityChest()
		if self.current_space >= 40:
			self.current_space %= 40
		if self.board[self.current_space] == 'G2J':
			self.current_space = 10
	def is_double(self, roll):
		return roll[0] == roll[1]
	def take_turn(self):
		roll = self.roll()
		num_roll = 1
		num_move = sum(roll)
		self.move(num_move)
		while self.is_double(roll) and num_roll < 3:
			roll = self.roll()
			num_roll = 1
			num_move = sum(roll)
			self.move(num_move)
		if num_roll == 3:
			self.current_space = self.board.index("JAIL")
		


play = monopoly(4)

times_landed = np.zeros(40,)
for l in range(10000000):
	play.take_turn()
	times_landed[play.current_space] += 1

probs = times_landed/sum(times_landed)

print np.argsort(probs)[-3:][::-1]
print probs[10], probs[24], probs[00]

