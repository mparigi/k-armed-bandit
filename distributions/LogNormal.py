import random

class LogNormal():
	def __init__(self, mean, stdev):
		self.mean = mean
		self.stdev = stdev

	def sample(self):
		return random.lognormvariate(mean, stdev)
