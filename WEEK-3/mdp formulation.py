Define States and Actions

states = ["Home", "Office", "Shop"]

actions = ["Left", "Right"]

print("States:", states)

print("Actions:", actions)




State Transition Table

transitions = {
    "Home": {
        "Right": "Office"
    },
    "Office": {
        "Left": "Home",
        "Right": "Shop"
    },
    "Shop": {
        "Left": "Office"
    }
}

print(transitions["Office"]["Right"])




Reward Function

rewards = {
    ("Home", "Right"): 5,
    ("Office", "Right"): 10,
    ("Shop", "Left"): 2
}

current_state = "Office"

action = "Right"

reward = rewards[(current_state, action)]

print("Reward:", reward)






Random Agent in an MDP

import random

states = ["A", "B", "C"]

actions = ["Left", "Right"]

state = random.choice(states)

action = random.choice(actions)

print("State:", state)

print("Action:", action)




Simple Episode Simulation

state = "Home"

transitions = {
    ("Home", "Right"): "Office",
    ("Office", "Right"): "Shop"
}

for step in range(2):

    state = transitions[(state, "Right")]

    print("Current State:", state)
