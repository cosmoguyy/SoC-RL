List comprehension

squares = []
for i in range(10):
    squares.append(i*i)


Dictionary Comprehensions
{
  1:1,
  2:4,
  3:9,
  4:16
}

squares = {i:i*i for i in range(1,5)}


Enumerate

fruits = ["apple","banana","mango"]

for i in range(len(fruits)):
    print(i, fruits[i])


ZIp

states = ["s0","s1","s2"]
rewards = [10,20,30]

for s,r in zip(states,rewards):
    print(s,r)


Lambda function

data = [
    ("A",5),
    ("B",2),
    ("C",9)
]

data.sort(key=lambda x:x[1])

print(data)



Args

def add(*args):
    return sum(args)

print(add(1,2,3,4))


kwargs

def student(**kwargs):
    print(kwargs)

student(name="Tanishq", age=18)

output: {'name':'Tanishq','age':18}


Classes

class Agent:

    def __init__(self,name):
        self.name = name

    def act(self):
        print("Taking action")

a = Agent("RL Agent")
a.act()


Reading files

with open("data.txt","r") as f:
    content = f.read()

print(content)


Exception Handling

try:
    x = int(input())
    print(x)
except ValueError:
    print("Not a number")


Random Actions

import random

action = random.choice([0,1])

print(action)


Q table

q_table = {}

q_table[(0,0)] = 5
q_table[(0,1)] = 3

print(q_table[(0,0)])


Best action selection 

q_values = [1.2, 3.4, 2.1]

best_action = q_values.index(max(q_values))

print(best_action)
