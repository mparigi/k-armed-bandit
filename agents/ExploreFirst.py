import numpy as np

class ExploreFirstAgent():
    def __init__(self, k, num_samples=8):
        self.num_samples = num_samples
        self.k = k
        self.num_times_selected = [0] * k
        self.rewards_per_action = [[] for _ in range(k)]

    def action(self):
        for action in range(self.k):
            if self.num_times_selected[action] < self.num_samples:
                return action
        
        # otherwise, exploit
        max_criterion = float('-inf')
        max_criterion_action = 0
        for action in range(self.k):
            mu = sum(self.rewards_per_action[action]) / len(self.rewards_per_action[action])
            sigma = np.std(self.rewards_per_action[action])
            criterion = mu + 3 * sigma
            if criterion > max_criterion:
                max_criterion = criterion
                max_criterion_action = action

        return max_criterion_action

    def update(self, action, reward):
        self.num_times_selected[action] += 1
        self.rewards_per_action[action].append(reward)