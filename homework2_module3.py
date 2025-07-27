import random

def get_numbers_ticket(min_value, max_value, quantity):

    if (
        not isinstance(min_value, int)
        or not isinstance(max_value, int)
        or not isinstance(quantity, int)
        or min_value < 1
        or max_value > 1000
        or min_value > max_value
        or quantity <= 0
        or quantity > (max_value - min_value + 1)
    ):
        return []

    
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)
