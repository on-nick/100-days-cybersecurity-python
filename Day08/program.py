import random

# Random float between 0 and 1
print("Random float:", random.random())

# Random number from range
print("Random range number:", random.randrange(1, 10))

# Random sample from a list
items = ["a", "b", "c", "d", "e"]
print("Random sample:", random.sample(items, 3))

# Seed example
random.seed(1)
print("Seeded random:", random.randint(1, 10))
print("Seeded random again:", random.randint(1, 10))
