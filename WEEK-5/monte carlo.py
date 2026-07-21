Episode Rewards

rewards = [1, 0, 2, 3]

G = sum(rewards)

print("Return:", G)




Monte Carlo State Value Update

returns = [10, 12, 8, 14]

value = sum(returns) / len(returns)

print("Estimated Value:", value)




First-Visit Monte Carlo

episode = ["A", "B", "C", "A"]

visited = set()

for state in episode:

    if state not in visited:

        print("First Visit:", state)

        visited.add(state)


WEEK 5 EXERCISE:


1.
Yes. First-visit and every-visit Monte Carlo converge to the same value function, although every-visit usually has slightly different learning dynamics.


2.
The Q-values for state 0 gradually stabilize after sufficient training episodes, with only small fluctuations afterward.
q_history = []

for ep in range(num_episodes):
    # existing training code

    q_history.append(Q[0].copy())

q_history = np.array(q_history)

for a in range(env.action_space.n):
    plt.plot(q_history[:, a], label=f"Action {a}")

plt.xlabel("Episode")
plt.ylabel("Q-value")
plt.legend()
plt.grid(True)
plt.show()



3.
Off-policy Monte Carlo successfully evaluates the greedy target policy while collecting experience using the random behaviour policy through importance sampling.
W = 1.0

for t in reversed(range(len(episode))):
    s, a, r = episode[t]
    G = gamma * G + r

    C[s, a] += W
    Q[s, a] += (W / C[s, a]) * (G - Q[s, a])

    greedy = np.argmax(Q[s])

    if a != greedy:
        break

    W *= 1.0 / behavior_policy[s, a]

