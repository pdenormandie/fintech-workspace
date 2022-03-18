import csv
from pathlib import Path

data = [
    {
        "first_name": "Jericho",
        "last_name": "Smith",
        "pin": 123
    },
    {
        "first_name": "Samantha",
        "last_name": "Jones",
        "pin": 456
    }
]

csvpath = Path("my_output.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data:
        csvwriter.writerow(row.values())
from pathlib import Path
import csv

csvpath = Path('my_output.csv')

with open (csvpath) as csvfile:
    data = csv.reader(csvfile)
    for row in data:
            print(row)