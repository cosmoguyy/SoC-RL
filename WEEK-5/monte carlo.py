Episode Rewards

rewards = [1, 0, 2, 3]

G = sum(rewards)

print("Return:", G)




Monte Carlo State Value Update

returns = [10, 12, 8, 14]

value = sum(returns) / len(returns)

print("Estimated Value:", value)




First-Visit Monte Carlo

episode = ["A", "B", "C", "A"]

visited = set()

for state in episode:

    if state not in visited:

        print("First Visit:", state)

        visited.add(state)
