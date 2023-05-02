
import random

def generate_random_number_between_a_and_b(a, b):
    if a == b:
        return a
    n = random.randint(a, b)
    if n < 0:
        print(n)
    return n

