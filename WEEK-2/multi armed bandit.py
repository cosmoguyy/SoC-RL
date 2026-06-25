Histogram with Custom Bins

import matplotlib.pyplot as plt

data = [12, 15, 18, 20, 22, 25, 28, 30, 35]

plt.hist(data, bins=5)

plt.title("Histogram")

plt.xlabel("Values")

plt.ylabel("Frequency")

plt.show()




Stacked Bar Chart

import matplotlib.pyplot as plt

students = ["A", "B", "C"]

maths = [80, 70, 90]

science = [75, 85, 80]

plt.bar(students, maths, label="Maths")

plt.bar(students, science, bottom=maths, label="Science")

plt.legend()

plt.title("Marks Comparison")

plt.show()
