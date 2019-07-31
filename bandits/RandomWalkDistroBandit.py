from .DistroBandit import DistroBandit
from distributions.Normal import Normal

class RandomWalkDistroBandit(DistroBandit):
	def __init__(self, distros, random_walk_distro=Normal(0, 0.01)):
		super().__init__(distros)
		self.random_walk_distro = random_walk_distro

	def select(self, j):
		action = super().select(j)
		# random walk to the distros
		for i in range(self.k):
			self.distros[i].mean += self.random_walk_distro.sample()
		return action

