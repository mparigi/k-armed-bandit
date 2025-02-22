import random

class Normal():
	def __init__(self, mean, stdev):
		self.mean = mean
		self.stdev = stdev

	def sample(self):
		return round(random.gauss(self.mean, self.stdev), 2)
