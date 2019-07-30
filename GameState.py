

class GameState():
	def __init__(self, bandit):
		self.bandit = bandit
		self.total_reward = 0

	def select(self, j):
		reward = self.bandit.select(j)
		self.total_reward += reward
		return reward