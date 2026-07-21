TD Target

reward = 5

gamma = 0.9

next_value = 10

td_target = reward + gamma * next_value

print(td_target)




TD Error

current_value = 8

td_target = 14

td_error = td_target - current_value

print(td_error)




TD Update

alpha = 0.1

value = 8

reward = 5

gamma = 0.9

next_value = 10

value = value + alpha * (reward + gamma * next_value - value)

print(value)



WEEK 5 EXERCISE:

1.
The TD error curve becomes much noisier because of the larger learning rate, but it can still converge, although less smoothly.

2.

def td_prediction_rw(n_episodes=300, alpha=0.1, gamma=1.0):
episodes = [1000, 5000, 10000]
v3 = []

for n in episodes:
    V = td_prediction_rw(n_episodes=n, alpha=0.1)
    v3.append(V[3])

plt.figure(figsize=(6,4))
plt.plot(episodes, v3, marker='o')
plt.axhline(0.5, color='red', linestyle='--', label='True Value')
plt.xlabel("Episodes")
plt.ylabel("V(3)")
plt.title("Convergence of V(3)")
plt.grid(True)
plt.legend()
plt.show()



3.
after td_prediction_rw().

def td_lambda_prediction_rw(n_episodes=300, alpha=0.1, gamma=1.0, lam=0.8):
    V = np.zeros(7)

    for _ in range(n_episodes):
        E = np.zeros(7)
        s = 3
        done = False

        while not done:
            ns, r, done = rw.step()

            target = r + (0 if done else gamma * V[ns])
            delta = target - V[s]

            E[s] += 1

            V += alpha * delta * E
            E *= gamma * lam

            s = ns

    return V

