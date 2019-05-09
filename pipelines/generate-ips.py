import random

for j in range(1000):
    numbers = []
    for k in range(4):
        numbers.append(str(random.randint(0, 255)))
    print(".".join(numbers))
