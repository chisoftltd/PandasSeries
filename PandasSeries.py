# Pandas Series

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print()

# Labels
print(myvar[0])
print()

# Create Labels
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print()

# When you have created labels, you can access an item by referring to the label
print(myvar["y"])
print()

# Key/Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)

print(myvar)
print()

# Create a Series using only data from "day1" and "day2"
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
print()

# DataFrames
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)