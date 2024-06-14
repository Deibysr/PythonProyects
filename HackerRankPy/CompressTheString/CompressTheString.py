from itertools import groupby

# Read input
S = input().strip()

# Use groupby to group consecutive characters
result = [(len(list(group)), int(key)) for key, group in groupby(S)]

# Prepare the output string
output = " ".join([f"({x}, {y})" for x, y in result])

# Print the result
print(output)
