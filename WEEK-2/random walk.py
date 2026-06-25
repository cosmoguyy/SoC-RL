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
