Policy Initialization

policy = {
    "A": "Left",
    "B": "Right",
    "C": "Left"
}

print(policy)




State Values

V = {
    "A": 0,
    "B": 0,
    "C": 0
}

print(V)




Policy Evaluation Step

reward = 10

gamma = 0.9

next_state_value = 5

value = reward + gamma * next_state_value

print(value)




Policy Improvement Step

Q_values = {
    "Left": 4,
    "Right": 8
}

best_action = max(Q_values, key=Q_values.get)

print(best_action)




Policy Update

policy = {
    "A": "Left"
}

policy["A"] = "Right"

print(policy)
