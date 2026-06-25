TD Target

reward = 5

gamma = 0.9

next_value = 10

td_target = reward + gamma * next_value

print(td_target)




TD Error

current_value = 8

td_target = 14

td_error = td_target - current_value

print(td_error)




TD Update

alpha = 0.1

value = 8

reward = 5

gamma = 0.9

next_value = 10

value = value + alpha * (reward + gamma * next_value - value)

print(value)
