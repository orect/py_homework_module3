import random

def get_numbers_ticket(min, max, quantity):
    result = set()

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

print(get_numbers_ticket(1, 100, 10))
    
    