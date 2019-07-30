import random

class EpsilonGreedyAgent():
	def __init__(self, k, epsilon):
		assert epsilon >= 0 and epsilon <= 1
		assert k > 0
		self.k = k
		self.epsilon = epsilon
		# (total reward gained from this action, times this action was selected)
		self.sample_average = [(0, 0)] * k

	def action(self):
		# decide if we explore or exploit
		explore = random.uniform(0, 1) <= self.epsilon

		if explore:
			# select a random action
			action = random.randint(0, self.k - 1)
		else: # exploit
			# find the action(s) with the highest Q value
			q_values = [0 if n == 0 else r / n for r, n in self.sample_average]
			max_q = max(q_values)
			best_action_indices = [i for i, j in enumerate(q_values) if j == max_q]
			action = random.choice(best_action_indices) # break ties randomly
		return action


	def update(self, action, reward):
		self.sample_average[action] = (self.sample_average[action][0] + reward, self.sample_average[action][1] + 1)