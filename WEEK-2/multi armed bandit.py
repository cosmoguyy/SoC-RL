Histogram with Custom Bins

import matplotlib.pyplot as plt

data = [12, 15, 18, 20, 22, 25, 28, 30, 35]

plt.hist(data, bins=5)

plt.title("Histogram")

plt.xlabel("Values")

plt.ylabel("Frequency")

plt.show()




Stacked Bar Chart

import matplotlib.pyplot as plt

students = ["A", "B", "C"]

maths = [80, 70, 90]

science = [75, 85, 80]

plt.bar(students, maths, label="Maths")

plt.bar(students, science, bottom=maths, label="Science")

plt.legend()

plt.title("Marks Comparison")

plt.show()




WEEK 2 Exercise:


1.
def softmax_action(Q, tau):
    exp_Q = np.exp((Q - np.max(Q)) / tau)
    probs = exp_Q / np.sum(exp_Q)
    return np.random.choice(len(Q), p=probs)

tau = 0.5
Q = np.zeros(k)

rewards = []

for t in range(steps):
    action = softmax_action(Q, tau)
    reward = bandit(action)
    rewards.append(reward)

    Q[action] += (reward - Q[action]) / (action_counts[action] + 1)
    action_counts[action] += 1

plt.figure(figsize=(8,4))
plt.plot(np.cumsum(rewards) / np.arange(1, len(rewards)+1))
plt.xlabel("Steps")
plt.ylabel("Average Reward")
plt.title("Softmax Action Selection")
plt.grid(True)
plt.show()

Softmax can outperform ε-greedy when the reward estimates are accurate because it prefers better actions probabilistically,
but performance depends on the choice of temperature τ.
  

2.

For c=0.1
https://colab.research.google.com/drive/1L6b1LptGkkykWjDFSir6zziVI_r8zgV8?usp=sharing

For c=10
https://colab.research.google.com/drive/1I-dZRC97N_mDSNkG612dwksOZFnEigFg?usp=sharing
With c = 0.1, UCB explores less and exploits earlier. With c = 10, UCB explores more before exploiting the best arm.


3.
Modified Bandit environment
class Bandit:
    def __init__(self, n_arms=10):
        self.n_arms = n_arms
        self.true_means = np.random.normal(0, 1, n_arms)  # hidden
        self.optimal_arm = np.argmax(self.true_means)

    def pull(self, arm):
        """Return a noisy reward for the chosen arm."""
        self.true_means += np.random.normal(0, 0.01, self.n_arms)  # Drift over time
        self.optimal_arm = np.argmax(self.true_means)              # Update optimal arm
        return np.random.normal(self.true_means[arm], 1.0)

bandit = Bandit(n_arms=10)
print("True arm means (hidden from agent):", np.round(bandit.true_means, 2))
print(f"Optimal arm: {bandit.optimal_arm} (mean={bandit.true_means[bandit.optimal_arm]:.2f})")

Strategies that continue to explore and use recent information (e.g., ε-greedy with a constant learning rate or UCB with ongoing exploration) 
handle non-stationary bandits better than purely greedy methods.
