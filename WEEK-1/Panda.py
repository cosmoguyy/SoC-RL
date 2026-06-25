Creating a DataFrame

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)

print(df)


Reading a CSV

import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())


View first row

print(df.head())



View last row

print(df.tail())


Select one column

print(df["Age"])


Filter Rows

print(df[df["Age"] > 20])



Multiple conditions

print(
    df[
        (df["Age"] > 18)
        &
        (df["Age"] < 22)
    ]
)



Value Count

print(df["Age"].value_counts())



Group by

df.groupby("Department")["Marks"].mean()
