class KArmedBandit():
	def __init__(self, k):
		self.k = k

	def select(self, j):
		raise NotImplementedError()