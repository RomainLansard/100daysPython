import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
randomize = random.randint(0, 4)
print(friends[randomize])

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))