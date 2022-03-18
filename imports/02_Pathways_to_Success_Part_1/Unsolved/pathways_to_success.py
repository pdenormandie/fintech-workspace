"""Pathways to Success."""
# @TODO: Import the Path tool from the pathlib library
# YOUR CODE HERE!
from pathlib import Path

# @TODO: Create a path to the `quarterly_data.csv` file
# YOUR CODE HERE!
csvpath = Path('quarterly_data.csv')

# Print the relative path (the relative location of the file)
print(f"The relative CSV path is {csvpath}")

# Print the absolute path (The absolute location of the file on the computer)
print(f"The absolute CSV path is {csvpath.absolute()}")

import csv
from pathlib import Path

csvpath = Path("quarterly_data.csv")
with open(csvpath) as csvfile:
        data = cs.reader(csvfile)
        for row in data:
            print(row)
            