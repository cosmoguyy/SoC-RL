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




Week 1 Exercise

1.
mu = 1.0
sigma = 0.5

https://colab.research.google.com/drive/1nJ-yZOqPUM3eDLNI0FXIBGG-ryl8Qluy?usp=sharing

Increasing μ (mean) shifts the histogram to the right, while decreasing μ shifts it to the left.
Increasing σ (standard deviation) makes the histogram wider and flatter, while decreasing σ makes it narrower and taller.

    
2.

true_mean = 1.0

samples = np.random.exponential(scale=true_mean, size=5000)
running_mean = np.cumsum(samples) / np.arange(1, len(samples) + 1)

plt.figure(figsize=(8, 3))
plt.plot(running_mean, color='steelblue', linewidth=1, label='Running mean')
plt.axhline(true_mean, color='tomato', linestyle='--', label=f'True mean = {true_mean}')
plt.xlabel('Number of samples')
plt.ylabel('Empirical mean')
plt.title('Law of Large Numbers — Exponential distribution')
plt.legend()
plt.tight_layout()
plt.show()

#Yes it still holds.

3.

N = 1000

flips = np.random.randint(0, 2, size=N)
running_fraction_heads = np.cumsum(flips) / np.arange(1, N + 1)

plt.figure(figsize=(8, 3))
plt.plot(running_fraction_heads, color='steelblue', linewidth=1, label='Running fraction of heads')
plt.axhline(0.5, color='tomato', linestyle='--', label='0.5')
plt.xlabel('Number of flips')
plt.ylabel('Fraction of heads')
plt.title('Running fraction of heads')
plt.legend()
plt.tight_layout()
plt.show()


It converge to 0.5
