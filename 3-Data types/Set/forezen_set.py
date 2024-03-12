fset = frozenset(["rawalpindi", "islamabad", "karachi",  "lahore"])

print(type(fset))

# fset.add("gujranwala") it will give error bcs frozen set can not change

sset = {"rawalpindi", "islamabad", "karachi",  "lahore"}

print(type(sset))

sset.add("faislabad")

print(sset)