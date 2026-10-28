import math
tree_circumfrence = int(input("Enter tree circumference in cm: "))
diameter = tree_circumfrence / math.pi
cut_down = diameter >= 50
print(f"Tree can be cut down: {cut_down}")