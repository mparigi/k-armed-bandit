from bandits.DistroBandit import DistroBandit
from distributions.Normal import Normal
from GameState import GameState

import random

def run_game(k):
	mean_low, mean_high = (-5, 5)
	stdev_low, stdev_high = (0, 3)
	distros = []
	for _ in range(k):
		distros.append(Normal(random.uniform(mean_low, mean_high), random.uniform(stdev_low, stdev_high)))
	bandit = DistroBandit(distros)

	game_state = GameState(bandit)

	print(f"This is the k-armed bandit game for k={k}.\nThe action rewards are sampled from normal distributions, which are randomly initialized for each action with each mean uniformly sampled from ({mean_low}, {mean_high}) and each standard deviation uniformly sampled from ({stdev_low}, {stdev_high}).")

	while True:
		selection = input("Select an Action...\n\t\ttotal reward - prints accumulated reward\n\t\t0-k - do an action\n\t\tquit - quit the game\n")
		if selection == "quit":
			print("Goodbye!")
			break
		elif selection.isdigit():
			if int(selection) >= game_state.bandit.k:
				print("Action out of range.")
				continue
			reward = game_state.select(int(selection))
			print(f"\tReward gained: {reward}")
		elif selection == "total reward":
			print(f"\tTotal Reward so far: {game_state.total_reward}")
		else:
			print("\tUnrecognized action, try again.")
		print("___")



if __name__ == "__main__":
	run_game(10)