Initialize Q Table

Q = {
    ("A", "Left"): 0,
    ("A", "Right"): 0
}

print(Q)




Choose Action

import random

action = random.choice(
    ["Left", "Right"]
)

print(action)




Observe Transition

state = "A"

action = "Right"

reward = 5

next_state = "B"

print(reward)




Q Learning Target

reward = 5

gamma = 0.9

max_next_q = 10

target = reward + gamma * max_next_q

print(target)




Q Learning Update

alpha = 0.1

Q_current = 8

Q_current = Q_current + alpha * (
    target - Q_current
)

print(Q_current)




Best Action

q_values = [2, 8]

best_action = q_values.index(
    max(q_values)
)

print(best_action)



WEEK 5 EXERCISE:


1.
Q-Learning may still converge eventually if every state-action pair has already been explored sufficiently, 
but starting with a purely greedy policy usually prevents adequate exploration.
SARSA is affected similarly and can also converge to a poor policy due to insufficient exploration.

                                                                                                          
                                                                                                          
2.
Increasing α makes learning noisier. Q-Learning typically becomes unstable sooner than SARSA because it updates toward the maximum estimated action value,
while SARSA updates using the action actually taken.
                                                                                                          

3.
Double Q-Learning generally reduces the overestimation bias seen in standard Q-Learning by separating action selection from action evaluation using two Q-tables.

def double_q_learning(env, episodes=5000, alpha=0.1, gamma=0.99, epsilon=0.1):
    Q1 = np.zeros((env.observation_space.n, env.action_space.n))
    Q2 = np.zeros((env.observation_space.n, env.action_space.n))

    for _ in range(episodes):
        s, _ = env.reset()
        done = False

        while not done:
            if np.random.rand() < epsilon:
                a = env.action_space.sample()
            else:
                a = np.argmax(Q1[s] + Q2[s])

            ns, r, terminated, truncated, _ = env.step(a)
            done = terminated or truncated

            if np.random.rand() < 0.5:
                best = np.argmax(Q1[ns])
                target = r + (0 if done else gamma * Q2[ns, best])
                Q1[s, a] += alpha * (target - Q1[s, a])
            else:
                best = np.argmax(Q2[ns])
                target = r + (0 if done else gamma * Q1[ns, best])
                Q2[s, a] += alpha * (target - Q2[s, a])

            s = ns

    return Q1 + Q2
