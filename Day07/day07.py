import random

# Random number between 1 and 10
num = random.randint(1, 10)
print("Random number:", num)

# Random choice from a list
colors = ["red", "blue", "green"]
print("Random color:", random.choice(colors))

# Shuffle a list
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print("Shuffled list:", items)
