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
