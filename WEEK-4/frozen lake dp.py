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




WEEK 4 EXERCISE:


1.
The win rate generally decreases because a smaller discount factor makes the agent more short-sighted, reducing the value of reaching the distant goal.


2.
link with 8x8 map: https://colab.research.google.com/drive/1W4nY8b12Ps-7vPHPuMtEoddthhjT8qV3?usp=sharing


3.
This no longer uses the transition model (env.P). Instead, it estimates values from sampled interactions with env.step(),
moving toward a model-free reinforcement learning approach.
    
def sample_backup(env, V, state, gamma):
    env.unwrapped.s = state

    q = np.zeros(env.action_space.n)

    for a in range(env.action_space.n):
        env.unwrapped.s = state
        ns, r, terminated, truncated, _ = env.step(a)
        done = terminated or truncated
        q[a] = r + (0 if done else gamma * V[ns])

    return q
    
