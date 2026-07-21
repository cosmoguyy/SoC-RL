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



WEEK 3 EXERCISE:

1.
States : 16
Actions : 4 (Left, Down, Right, Up)
Terminal States: All hole states and the goal state.

    
2.
Tic-Tac-Toe can be modeled as an MDP using the above definitions of S, A, R, and T.
States : All valid board configurations.
Actions : Place a mark (X or O) in any empty cell.
Rewards :
+1 for a win
0 for a draw
-1 for a loss
Transition Function (T): Applying a valid move changes the board state and then the opponent makes a move.


3.
episodes = 1000
episode_rewards = []

for _ in range(episodes):
    state = "high"
    total_reward = 0

    for _ in range(100):
        if state == "high":
            total_reward += r_search
            if np.random.rand() < alpha:
                state = "high"
            else:
                state = "low"
        else:
            total_reward += r_search
            if np.random.rand() < beta:
                state = "low"
            else:
                state = "high"

    episode_rewards.append(total_reward)

plt.hist(episode_rewards, bins=30)
plt.xlabel("Total Undiscounted Reward")
plt.ylabel("Episodes")
plt.title("Always Search Policy")
plt.grid(True)
plt.show()
