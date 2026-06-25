Create arrays

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr)


Zeros array

import numpy as np

arr = np.zeros(5)

print(arr)


Ones array

arr = np.ones(5)

print(arr)



Range of numbers

arr = np.arange(0, 10)

print(arr)



# Reshape array

arr = np.arange(12)

matrix = arr.reshape(3, 4)

print(matrix)



# Random numbers

arr = np.random.rand(5)

print(arr)



# Random integers

arr = np.random.randint(1, 10, size=5)

print(arr)



# Array addition

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

print(a + b)



# Array multiplication

a = np.array([1, 2, 3])

print(a * 2)



# Element-wise multiplication

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

print(a * b)



# Mean

arr = np.array([10, 20, 30])

print(np.mean(arr))



# Sum

print(np.sum(arr))



# Maximum and Minimum

print(np.max(arr))

print(np.min(arr))



# Indexing

arr = np.array([10, 20, 30, 40])

print(arr[2])



# Slicing

print(arr[1:3])



# Matrix creation

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)



# Matrix indexing

print(matrix[1, 2])



# Transpose matrix

print(matrix.T)



# Dot product

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

print(np.dot(a, b))



# Find index of maximum value

q_values = np.array([1.2, 4.5, 2.3])

action = np.argmax(q_values)

print(action)



# Boolean filtering

arr = np.array([10, 20, 30, 40])

print(arr[arr > 20])



# Normalize data

arr = np.array([10, 20, 30])

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print(normalized)



# Identity matrix

I = np.eye(3)

print(I)



# Q-table

q_table = np.zeros((5, 2))

print(q_table)



# Choose best action

q_table = np.array([
    [1.0, 3.5],
    [2.2, 1.8]
])

state = 0

action = np.argmax(q_table[state])

print(action)
