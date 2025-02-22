import random

class EpsilonGreedyAgent():
	def __init__(self, k, epsilon=0.2):
		assert epsilon >= 0 and epsilon <= 1
		assert k > 0
		self.k = k
		self.epsilon = epsilon
		# (Q(i), num times selected)
		self.q_values = [(0, 0)] * k

	def action(self):
		# decide if we explore or exploit
		explore = random.uniform(0, 1) <= self.epsilon

		if explore:
			# select a random action
			action = random.randint(0, self.k - 1)
		else: # exploit
			# find the action(s) with the highest Q value
			max_q = max(self.q_values)
			best_action_indices = [i for i, j in enumerate(self.q_values) if j == max_q]
			action = random.choice(best_action_indices) # break ties randomly
		return action


	def update(self, action, reward):
		raise NotImplementedError()

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


class EpsilonGreedySampleAverageAgent(EpsilonGreedyAgent):
	def update(self, action, reward):
		old_q, old_n = self.q_values[action]
		self.q_values[action] = (
			old_q + (1/(old_n + 1)) * (reward - old_q), # Q update rule
			old_n + 1
			)
			