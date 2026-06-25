Create Frozen Lake States

states = list(range(16))

print(states)




Initialize Value Function

V = [0] * 16

print(V)




Initialize Random Policy

policy = ["Right"] * 16

print(policy)




Terminal State Check

state = 15

if state == 15:

    print("Goal State")




State Reward

rewards = [0] * 15 + [1]

print(rewards[15])




Policy Lookup

policy = {
    0: "Right",
    1: "Down",
    2: "Right"
}

print(policy[1])




Value Update

reward = 1

gamma = 0.9

next_state_value = 10

new_value = reward + gamma * next_state_value

print(new_value)
