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



WEEK 4 EXERCISE: 
1.

As γ increases, the value function spreads farther from the goal because future rewards are weighted more heavily.


2.
Policy: 
policy = np.full(env.n_states(), 2)

States in the rightmost column repeatedly hit the boundary, so the agent keeps attempting to move right and cannot make further progress.


3.
theta = 1e-6

while True:
    delta = 0

    for s in range(env.n_states()):
        if s in terminal_states:
            continue

        v = V[s]

        a = policy[s]
        ns, r, done = transitions[s][a]

        V[s] = r + gamma * V[ns] * (not done)

        delta = max(delta, abs(v - V[s]))

    if delta < theta:
        break


Yes. In-place policy evaluation typically converges faster because updated state values are used immediately within the same iteration.
