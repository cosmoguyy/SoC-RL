Error Bar Plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [10, 15, 13, 17, 20]

error = [1, 2, 1, 2, 1]

plt.errorbar(x, y, yerr=error)

plt.title("Error Bar Plot")

plt.show()




Stem Plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [3, 7, 2, 8, 5]

plt.stem(x, y)

plt.title("Stem Plot")

plt.show()




Reward Distribution

import numpy as np

import matplotlib.pyplot as plt

rewards = np.random.normal(50, 10, 100)

plt.hist(rewards, bins=10)

plt.xlabel("Reward")

plt.ylabel("Frequency")

plt.title("Reward Distribution")

plt.show()


WEEK 2 EXERCISE:


1.
N_WALKS = 1000
plus20 = 0
minus20 = 0

for _ in range(N_WALKS):
    position = 0

    while -20 < position < 20:
        position += np.random.choice([-1, 1])

    if position == 20:
        plus20 += 1
    else:
        minus20 += 1

print("Fraction ending at +20:", plus20 / N_WALKS)
print("Fraction ending at -20:", minus20 / N_WALKS)

Approximately half of the walks end at +20 and half at −20.



2. Adding a 2D random walk
plt.figure(figsize=(6,6))

for _ in range(5):
    x = [0]
    y = [0]

    for _ in range(100):
        move = np.random.choice(["up", "down", "left", "right"])

        if move == "up":
            x.append(x[-1])
            y.append(y[-1] + 1)
        elif move == "down":
            x.append(x[-1])
            y.append(y[-1] - 1)
        elif move == "left":
            x.append(x[-1] - 1)
            y.append(y[-1])
        else:
            x.append(x[-1] + 1)
            y.append(y[-1])

    plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Random Walk")
plt.axis("equal")
plt.grid(True)
plt.show()


3.Implementing the 5-state random walk.

states = ['A', 'B', 'C', 'D', 'E']
true_values = np.array([1, 2, 3, 4, 5]) / 6

print("Analytical True Values:")
for s, v in zip(states, true_values):
    print(f"{s}: {v:.3f}")

empirical = np.zeros(5)
episodes = 10000

for _ in range(episodes):
    state = 2
    visited = []

    while 0 <= state <= 4:
        visited.append(state)
        state += np.random.choice([-1, 1])

    reward = 1 if state == 5 else 0

    for s in visited:
        empirical[s] += reward

empirical /= episodes

print("\nEmpirical Values:")
for s, v in zip(states, empirical):
    print(f"{s}: {v:.3f}")


The empirical state values closely match the analytical values [1/6, 2/6, 3/6, 4/6, 5/6].
