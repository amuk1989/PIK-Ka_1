from typing import List

def equal(numbers: List[float], value: float, accuracy: int = 0):
    for number in numbers:
        if round(number,accuracy) == round(value,accuracy):
            return True
    return False