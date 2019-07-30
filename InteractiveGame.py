from bandits.DistroBandit import DistroBandit
from distributions.Normal import Normal


class GameState():
	def __init__(self, bandit):
		self.bandit = bandit
		self.total_reward = 0

	def select(self, j):
		reward = self.bandit.select(j)
		self.total_reward += reward
		return reward

def run_game(k):
	distros = [Normal(random.uniform(-5, 5), random.uniform(0, 3))] * k
	bandit = DistroBandit(distros)

	game_state = GameState(bandit)

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