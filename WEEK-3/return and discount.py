Calculate Total Return

rewards = [10, 5, 2]

G = sum(rewards)

print("Return:", G)



Discounted Return

rewards = [10, 5, 2]

gamma = 0.9

G = 0

for t in range(len(rewards)):

    G += (gamma ** t) * rewards[t]

print("Discounted Return:", round(G, 2))



Effect of Different Gamma Values

reward = 100

gamma1 = 0.5

gamma2 = 0.9

future_reward_1 = gamma1 * reward

future_reward_2 = gamma2 * reward

print("Gamma 0.5:", future_reward_1)

print("Gamma 0.9:", future_reward_2)


