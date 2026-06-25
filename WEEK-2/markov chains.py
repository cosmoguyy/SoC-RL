Box Plot

import matplotlib.pyplot as plt

data = [12, 15, 14, 18, 21, 19, 17, 16, 14]

plt.boxplot(data)

plt.title("Box Plot")

plt.show()




Subplots

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [1, 4, 9, 16]

y2 = [16, 9, 4, 1]

plt.subplot(1, 2, 1)

plt.plot(x, y1)

plt.title("Plot 1")

plt.subplot(1, 2, 2)

plt.plot(x, y2)

plt.title("Plot 2")

plt.show()




Scatter Plot with Colors

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [5, 7, 3, 8, 4]

colors = [10, 20, 30, 40, 50]

plt.scatter(x, y, c=colors)

plt.colorbar()

plt.show()
