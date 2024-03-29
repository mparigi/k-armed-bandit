from bandits.DistroBandit import DistroBandit
from distributions.Normal import Normal
from GameState import GameState
from agents.EpsilonGreedySampleAverageAgent import EpsilonGreedySampleAverageAgent

import random

def run_game(k, timesteps, verbose=False):
	mean_low, mean_high = (-5, 5)
	stdev_low, stdev_high = (0, 3)

	distros = []
	for _ in range(k):
		distros.append(Normal(random.uniform(mean_low, mean_high), random.uniform(stdev_low, stdev_high)))

	# determine optimal action
	highest_mean = distros[0].mean
	optimal_action = 0
	for i, d in enumerate(distros):
		if d.mean > highest_mean:
			highest_mean = d.mean
			optimal_action = i

	bandit = DistroBandit(distros)

	game_state = GameState(bandit)
	agent = EpsilonGreedySampleAverageAgent(k)

	print(f"This is the k-armed bandit game for k={k}.\nThe action rewards are sampled from normal distributions, which are randomly initialized for each action with each mean uniformly sampled from ({mean_low}, {mean_high}) and each standard deviation uniformly sampled from ({stdev_low}, {stdev_high}).")

	optimal_stats = (0, 0) # num optimal, total

	print(f"The optimal action is action {optimal_action} with mean {highest_mean} and stdev {distros[optimal_action].stdev}")
	print("*")
	for _ in range(timesteps):
		action = agent.action()
		reward = game_state.select(action)
		optimal_stats = (optimal_stats[0] + (1 if action == optimal_action else 0), optimal_stats[1] + 1)
		if verbose:
			print(f"Agent chose action {action} and got a reward of {reward}.")
		agent.update(action, reward)

	print("*")
	print("Agent's Total Reward: ", game_state.total_reward)
	print(f"The Agent chose the optimal action {(optimal_stats[0] / optimal_stats[1]) * 100}% of the time")
	print(f"If the Agent had chose the optimal action every time, we would expect a total reward of {highest_mean * timesteps}.")



if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser(description='play agent against k-armed bandit problem.')
	parser.add_argument("-v", "--verbose", help="print agent actions and rewards.", action="store_true")
	parser.add_argument("k", type=int, help="the number of actions.")
	parser.add_argument("timesteps", type=int, help="the number of timesteps, or actions taken.")
	args = parser.parse_args()

	run_game(args.k, args.timesteps, args.verbose)