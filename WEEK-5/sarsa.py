Initialize Q Table

Q = {
    ("A", "Left"): 0,
    ("A", "Right"): 0,
    ("B", "Left"): 0,
    ("B", "Right"): 0
}

print(Q)




Choose Action

import random

actions = ["Left", "Right"]

action = random.choice(actions)

print(action)




Epsilon Greedy Action

import random

epsilon = 0.2

if random.random() < epsilon:

    action = random.choice(["Left", "Right"])

else:

    action = "Right"

print(action)




Observe Reward

reward = 5

next_state = "B"

print(reward)

print(next_state)




Choose Next Action

actions = ["Left", "Right"]

next_action = random.choice(actions)

print(next_action)




SARSA Target

reward = 5

gamma = 0.9

Q_next = 10

target = reward + gamma * Q_next

print(target)




SARSA Update

alpha = 0.1

Q_current = 8

reward = 5

gamma = 0.9

Q_next = 10

Q_current = Q_current + alpha * (
    reward + gamma * Q_next - Q_current
)

print(Q_current)




Store Experience

state = "A"

action = "Right"

reward = 5

next_state = "B"

next_action = "Left"

experience = (
    state,
    action,
    reward,
    next_state,
    next_action
)

print(experience)
