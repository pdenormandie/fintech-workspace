films = {
    "Nic": 105,
    "Betty": 114,
    "Dwayne": 70
}

print("Nicolas Cage Films: ", films["Nic"])
print("Betty White Films: ", films["Betty"])
print("Dwayne Johnson Films: ", films["Dwayne"])
top_traders_per_month = {}
top_traders_per_month["January"] = "Susan"
top_traders_per_month["February"] = "Samuel"

print(top_traders_per_month)
top_traders_per_month["February"] = "Harold"
print(top_traders_per_month)
del top_traders_per_month["February"]
print(top_traders_per_month)
