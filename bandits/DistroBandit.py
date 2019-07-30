from .KArmedBandit import KArmedBandit

class DistroBandit(KArmedBandit):
	def __init__(self, distros):
		super().__init__(len(distros))
		self.distros = distros

	def select(self, j):
		# selected action needs to be in range
		assert(j < self.k)

		# take the j'th action
		return self.distros[j].sample()
