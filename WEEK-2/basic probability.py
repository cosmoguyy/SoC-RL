Learning Curve

import matplotlib.pyplot as plt

episodes = [1, 2, 3, 4, 5, 6, 7]

accuracy = [55, 60, 68, 75, 82, 88, 92]

plt.plot(episodes, accuracy)

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.title("Learning Curve")

plt.show()




Compare Two Algorithms

import matplotlib.pyplot as plt

episodes = [1, 2, 3, 4, 5]

algo1 = [10, 20, 35, 50, 60]

algo2 = [5, 18, 30, 45, 58]

plt.plot(episodes, algo1, label="Q-Learning")

plt.plot(episodes, algo2, label="SARSA")

plt.legend()

plt.xlabel("Episodes")

plt.ylabel("Reward")

plt.title("Algorithm Comparison")

plt.show()




Moving Average Reward

import numpy as np

import matplotlib.pyplot as plt

rewards = [10, 25, 15, 40, 35, 50, 45, 60]

window = 3

moving_avg = np.convolve(
    rewards,
    np.ones(window)/window,
    mode='valid'
)

plt.plot(moving_avg)

plt.xlabel("Episodes")

plt.ylabel("Average Reward")

plt.title("Moving Average Reward")

plt.show()
