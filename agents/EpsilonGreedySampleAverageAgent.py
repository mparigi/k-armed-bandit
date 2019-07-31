from .EpsilonGreedyAgent import EpsilonGreedyAgent

class EpsilonGreedySampleAverageAgent(EpsilonGreedyAgent):
	def update(self, action, reward):
		old_q, old_n = self.q_values[action]
		self.q_values[action] = (
			old_q + (1/(old_n + 1)) * (reward - old_q), # Q update rule
			old_n + 1
			)