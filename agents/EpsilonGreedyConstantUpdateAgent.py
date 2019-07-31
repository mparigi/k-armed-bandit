from .EpsilonGreedyAgent import EpsilonGreedyAgent

class EpsilonGreedyConstantUpdateAgent(EpsilonGreedyAgent):
	def __init__(self, k, epsilon=0.2, update_alpha=0.1):
		super().__init__(k, epsilon)
		self.update_alpha = update_alpha

	def update(self, action, reward):
		old_q, old_n = self.q_values[action]
		self.q_values[action] = (
			old_q + (self.update_alpha) * (reward - old_q), # constant step size
			old_n + 1
			)
