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



WEEK 1 Exercise

1.

T_absorbing = np.array([
    [1.0, 0.0, 0.0],
    [0.2, 0.6, 0.2],
    [0.2, 0.3, 0.5]
])

eigvals, eigvecs = np.linalg.eig(T_absorbing.T)
idx = np.argmin(np.abs(eigvals - 1))
pi = eigvecs[:, idx].real
pi = pi / pi.sum()

print("Stationary distribution:", pi)

The stationary distribution converges to Rainy = 1, Sunny = 0, Cloudy = 0.


2.
states = ["Rainy", "Sunny", "Cloudy", "Stormy"]

T = np.array([
    [0.5, 0.2, 0.2, 0.1],
    [0.2, 0.5, 0.2, 0.1],
    [0.2, 0.3, 0.4, 0.1],
    [0.3, 0.1, 0.2, 0.4]
])

print("Row sums:", T.sum(axis=1))

The Markov chain successfully works with four states, including the new Stormy state, and the state probabilities converge to a stationary distribution.
link to 4 state notebook: https://colab.research.google.com/drive/1WmJ6qbUL9GuEEXLV2q1EJ0atGMQJB71z?usp=sharing


3.
eigvals, eigvecs = np.linalg.eig(T.T)
idx = np.argmin(np.abs(eigvals - 1))
pi = eigvecs[:, idx].real
pi = pi / pi.sum()

print("π =", pi)
print("πT =", pi @ T)

assert np.allclose(pi @ T, pi)
print("Verified: π @ T = π")
