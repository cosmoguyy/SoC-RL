Line plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.show()




Line plot with labels

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlabel("X-axis")

plt.ylabel("Y-axis")

plt.title("Simple Line Plot")

plt.show()




Change line style

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y = [1, 4, 9, 16]

plt.plot(x, y, linestyle="--")

plt.show()




Change marker style

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y = [1, 4, 9, 16]

plt.plot(x, y, marker="o")

plt.show()




Scatter plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [5, 3, 8, 4, 7]

plt.scatter(x, y)

plt.show()




Bar chart

import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]

marks = [90, 80, 70, 85]

plt.bar(students, marks)

plt.show()




Horizontal bar chart

import matplotlib.pyplot as plt

students = ["A", "B", "C"]

marks = [90, 80, 70]

plt.barh(students, marks)

plt.show()




Histogram

import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

plt.hist(data)

plt.show()




Pie chart

import matplotlib.pyplot as plt

sizes = [40, 30, 20, 10]

labels = ["A", "B", "C", "D"]

plt.pie(sizes, labels=labels)

plt.show()




Multiple lines

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [1, 2, 3, 4]

y2 = [4, 3, 2, 1]

plt.plot(x, y1)

plt.plot(x, y2)

plt.show()




Add legend

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [1, 2, 3, 4]

y2 = [4, 3, 2, 1]

plt.plot(x, y1, label="Increasing")

plt.plot(x, y2, label="Decreasing")

plt.legend()

plt.show()




Grid

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y = [1, 4, 9, 16]

plt.plot(x, y)

plt.grid()

plt.show()




Save figure

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y = [1, 4, 9, 16]

plt.plot(x, y)

plt.savefig("graph.png")

plt.show()




Figure size

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y = [1, 4, 9, 16]

plt.figure(figsize=(8, 4))

plt.plot(x, y)

plt.show()




Random scatter plot

import numpy as np

import matplotlib.pyplot as plt

x = np.random.rand(50)

y = np.random.rand(50)

plt.scatter(x, y)

plt.show()




Plot rewards of an RL agent

import matplotlib.pyplot as plt

rewards = [10, 20, 15, 35, 40, 50]

episodes = [1, 2, 3, 4, 5, 6]

plt.plot(episodes, rewards)

plt.xlabel("Episodes")

plt.ylabel("Reward")

plt.title("Reward Curve")

plt.show()




Q-values bar chart

import matplotlib.pyplot as plt

actions = ["Left", "Right"]

q_values = [2.5, 5.8]

plt.bar(actions, q_values)

plt.title("Q Values")

plt.show()
```

