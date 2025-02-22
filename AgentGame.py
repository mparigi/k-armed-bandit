from bandits.DistroBandit import DistroBandit
from distributions.Normal import Normal
from GameState import GameState
from agents.ExploreFirst import ExploreFirstAgent
import numpy as np
import argparse

import random


def run_game(k, timesteps, verbose=False):
    mean_low, mean_high = (8, 16)
    stdev_low, stdev_high = (2, 6)

    distros = []
    for _ in range(k):
        distros.append(
            Normal(
                round(random.uniform(mean_low, mean_high), 2),
                round(random.uniform(stdev_low, stdev_high), 2),
            )
        )

    bandit = DistroBandit(distros)

    game_state = GameState(bandit)
    agent = ExploreFirstAgent(k, num_samples=10)

    print(
        f"This is the k-armed bandit game for k={k}.\nThe action rewards are sampled from normal distributions, which are randomly initialized for each action with each mean uniformly sampled from ({mean_low}, {mean_high}) and each standard deviation uniformly sampled from ({stdev_low}, {stdev_high})."
    )

    if verbose:
        for i, d in enumerate(distros):
            print(f"Action {i} has mean {d.mean} and stdev {d.stdev}")

    print("*")
    for t in range(timesteps):
        action = agent.action()
        reward = game_state.select(action)
        if verbose:
            print(f"timestep {t}: ")
            print(f"Agent chose action {action} and got a reward of {reward}.")
        agent.update(action, reward)

    print("*")
    print("Agent's Return: \t\t", game_state.total_reward)
    print("Agent's Average Reward: \t", game_state.total_reward / timesteps)
    print("----")

    return game_state.total_reward


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="play agent against k-armed bandit problem."
    )
    parser.add_argument(
        "-v", "--verbose", help="print agent actions and rewards.", action="store_true"
    )
    parser.add_argument("k", type=int, help="the number of actions.")
    parser.add_argument(
        "timesteps", type=int, help="the number of timesteps, or actions taken."
    )
    args = parser.parse_args()

    returns = []
    for _ in range(10):
        returns.append(run_game(args.k, args.timesteps, args.verbose))

    print("\n----------\n")
    print(f"over {len(returns)} runs,")

    print(f"Average Return: \t\t{sum(returns) / len(returns)}")
    print(f"Standard Deviation of Return: \t{np.std(returns)}")
