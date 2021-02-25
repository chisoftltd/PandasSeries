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