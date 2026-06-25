Policy Representation

policy = {
    "A": "Right",
    "B": "Right",
    "C": "Left"
}

print(policy)




State Values

V = {
    "A": 0,
    "B": 5,
    "C": 10
}

print(V)




Follow Policy

policy = {
    "A": "Right",
    "B": "Left"
}

state = "A"

action = policy[state]

print(action)




Update State Value

V = {
    "A": 0
}

reward = 10

gamma = 0.9

next_state_value = 5

V["A"] = reward + gamma * next_state_value

print(V["A"])
